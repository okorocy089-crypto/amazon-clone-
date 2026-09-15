from django.shortcuts import get_object_or_404, redirect, render
from django.core.exceptions import ValidationError
from django.http import JsonResponse
from django.db import transaction
from .models import Cart, CartItem
from catalog.models import Product
from orders.models import Order, OrderItem
 
 
def get_current_cart(request):
    """
    Returns the Cart belonging to whoever is making this request —
    a real user if logged in, otherwise their anonymous session.
    Creates one if it doesn't exist yet.
    """
    if request.user.is_authenticated:
        cart, _ = Cart.objects.get_or_create(user=request.user)
    else:
        if not request.session.session_key:
            request.session.create()
        cart, _ = Cart.objects.get_or_create(session_key=request.session.session_key)
    return cart
 
 
def add_to_cart_view(request, product_id):
    if request.method != "POST":
        return redirect("homepage")
 
    product = get_object_or_404(Product, id=product_id)
    cart = get_current_cart(request)
 
    item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        item.quantity += 1
    # else: a brand-new CartItem already starts at quantity=1 (its model default)
 
    try:
        item.full_clean()  # runs CartItem.clean() — the stock-limit check
    except ValidationError as e:
        return JsonResponse({"error": e.messages}, status=400)
 
    item.save()
 
    cart_count = sum(i.quantity for i in cart.items.all())
    return JsonResponse({"success": True, "cart_count": cart_count})


def _get_owned_item(request, item_id):
    """Fetch a CartItem, but only if it actually belongs to the current
    visitor's cart — stops one user from tampering with another's item
    just by guessing/reusing a UUID in the request."""
    cart = get_current_cart(request)
    return get_object_or_404(CartItem, id=item_id, cart=cart)


def increase_quantity_view(request, item_id):
    if request.method != "POST":
        return redirect("cart_page")

    item = _get_owned_item(request, item_id)
    item.quantity += 1

    try:
        item.full_clean()
    except ValidationError as e:
        return JsonResponse({"error": e.messages}, status=400)

    item.save()
    return JsonResponse({"success": True})


def decrease_quantity_view(request, item_id):
    if request.method != "POST":
        return redirect("cart_page")

    item = _get_owned_item(request, item_id)

    if item.quantity <= 1:
        item.delete()  # decrementing below 1 means the item leaves the cart
    else:
        item.quantity -= 1
        item.save()

    return JsonResponse({"success": True})


def remove_item_view(request, item_id):
    if request.method != "POST":
        return redirect("cart_page")

    item = _get_owned_item(request, item_id)
    item.delete()
    return JsonResponse({"success": True})


def remove_all_view(request):
    if request.method != "POST":
        return redirect("cart_page")

    cart = get_current_cart(request)
    cart.items.all().delete()
    return JsonResponse({"success": True})
 
 
def merge_guest_cart_into_user(request, user):
    """
    Call this right after a successful login (or the auto-login at the end
    of registration). If the visitor had a guest cart tied to their browser
    session, its contents get folded into their real account's cart.
    """
    session_key = request.session.session_key
    if not session_key:
        return
 
    try:
        guest_cart = Cart.objects.get(session_key=session_key)
    except Cart.DoesNotExist:
        return  # nothing to merge
 
    user_cart, _ = Cart.objects.get_or_create(user=user)
 
    for guest_item in guest_cart.items.all():
        user_item, created = CartItem.objects.get_or_create(
            cart=user_cart, product=guest_item.product
        )
        if created:
            user_item.quantity = guest_item.quantity
        else:
            user_item.quantity += guest_item.quantity
 
        # The two carts might each have been within stock limits on their
        # own, but combined could now exceed it — clamp to what's available.
        if user_item.quantity > user_item.product.quantity:
            user_item.quantity = user_item.product.quantity
 
        user_item.save()
 
    guest_cart.delete()


def cart_page_view(request):
    cart = get_current_cart(request)
    items = cart.items.all()
    total = sum(item.product.price * item.quantity for item in items)

    return render(request, "cart/cart.html", {
        "items": items,
        "total": total,
        "hide_bottom_nav": True,
    })


def checkout(request):
    if not request.user.is_authenticated:
        return redirect("register")

    cart = get_current_cart(request)
    items = cart.items.all()
    if not items:
        return redirect("cart_page")

    if not hasattr(request.user, "paymentcard"):
        return redirect("add_card")

    if request.method == "POST":
        try:
            with transaction.atomic():
                for item in items:
                    product = item.product
                    if product.quantity < item.quantity:
                        raise ValueError(f"Insufficient stock for {product.name}")
                    product.quantity -= item.quantity
                    product.save()

                total = sum(item.product.price * item.quantity for item in items)
                order = Order.objects.create(user=request.user, total=total)

                for item in items:
                    OrderItem.objects.create(
                        order=order,
                        product=item.product,
                        product_name=item.product.name,
                        product_price=item.product.price,
                        quantity=item.quantity,
                    )

                cart.items.all().delete()
        except ValueError as e:
            return JsonResponse({"error": str(e)}, status=400)

        return redirect("receipt", order_id=order.id)

    total = sum(item.product.price * item.quantity for item in items)
    return render(request, "cart/checkout.html", {
        "items": items,
        "cart": cart,
        "cart_total": total,
    })
