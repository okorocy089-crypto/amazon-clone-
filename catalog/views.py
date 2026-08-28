from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from django.http import JsonResponse

def category_results_view(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category)
    return render(request, "catalog/category_results.html", {
        "category": category,
        "products": products,
    })


def product_detail_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, "catalog/product_detail.html", {
        "product": product,
    })


def search_suggestions(request):
    query = request.GET.get('q', '')
    products = Product.objects.filter(name__icontains=query)[:10]
    suggestions = [{'id': p.id, 'name': p.name, 'price': str(p.price)} for p in products]
    return JsonResponse(suggestions, safe=False)

def search_results(request):
    query = request.GET.get('q', '')
    products = Product.objects.filter(name__icontains=query)
    return render(request, 'catalog/search.html', {'query': query, 'results': products}) # the file needs to live at catalog/templates/catalog/search.html

