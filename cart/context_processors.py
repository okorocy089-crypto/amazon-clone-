from .models import Cart
from catalog.models import Category


def cart_count(request):
    """
    Makes {{ cart_count }} available in every template automatically.
    Deliberately does NOT create a Cart if one doesn't exist yet — a
    visitor who's only browsing shouldn't get an empty Cart row created
    just from viewing a page.
    """
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user).first()
    else:
        session_key = request.session.session_key
        cart = Cart.objects.filter(session_key=session_key).first() if session_key else None

    count = sum(item.quantity for item in cart.items.all()) if cart else 0
    return {"cart_count": count, "all_categories": Category.objects.all()}