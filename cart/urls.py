from django.urls import path
from . import views
 
urlpatterns = [
    path("", views.cart_page_view, name="cart_page"),
    path("add/<uuid:product_id>/", views.add_to_cart_view, name="add_to_cart"),
    path("increase/<uuid:item_id>/", views.increase_quantity_view, name="increase_quantity"),
    path("decrease/<uuid:item_id>/", views.decrease_quantity_view, name="decrease_quantity"),
    path("remove/<uuid:item_id>/", views.remove_item_view, name="remove_item"),
    path("remove-all/", views.remove_all_view, name="remove_all"),
    path("checkout/", views.checkout, name="checkout"),
]