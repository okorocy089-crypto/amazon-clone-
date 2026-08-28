from . import views

from django.urls import path
from . import views

urlpatterns = [
    path("category/<uuid:category_id>/", views.category_results_view, name="category_results"),
    path("product/<uuid:product_id>/", views.product_detail_view, name="product_detail"),
    path("search/", views.search_results, name="search_results"),
    path("search/suggestions/", views.search_suggestions, name="search_suggestions"),
]