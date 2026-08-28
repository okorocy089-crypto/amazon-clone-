from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from collections import defaultdict
from .models import Order

# Create your views here.
def receipt(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    if not request.session.get(f'receipt_viewed_{order_id}'):
        request.session[f'receipt_viewed_{order_id}'] = True
    else:
        return redirect('order_history')  # Prevent re-view
    
    return render(request, 'orders/receipt.html', {'order': order})

@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    
    from collections import defaultdict
    grouped = defaultdict(list)
    for order in orders:
        date_key = order.created_at.date()
        grouped[date_key].append(order)
    
    return render(request, 'orders/order_history.html', {'grouped_orders': dict(grouped)})
