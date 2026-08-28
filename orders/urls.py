from django.urls import path
from . import views

urlpatterns = [
    path("history/", views.order_history, name="order_history"),
    path("receipt/<uuid:order_id>/", views.receipt, name="receipt"),
]