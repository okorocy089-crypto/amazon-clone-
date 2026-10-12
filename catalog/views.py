from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from django.http import JsonResponse
from django.db.models import Q


def _search_products(query):
    terms = query.split()
    if not terms:
        return Product.objects.none(), False

    prefix_matches = Product.objects.filter(name__istartswith=query).order_by("name")
    if len(query) == 1 or prefix_matches.exists():
        return prefix_matches, False

    matches = Product.objects.all()
    for term in terms:
        matches = matches.filter(name__icontains=term)
    matches = matches.order_by("name")
    if matches.exists():
        return matches, True

    related_query = Q()
    for term in terms:
        related_query |= Q(name__icontains=term)
    related = Product.objects.filter(related_query).order_by("name")
    return related, related.exists()

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
    query = request.GET.get('q', '').strip()
    if not query:
        return JsonResponse([], safe=False)

    products, _ = _search_products(query)
    suggestions = [{'id': p.id, 'name': p.name, 'price': str(p.price)} for p in products]
    return JsonResponse(suggestions, safe=False)

def search_results(request):
    query = request.GET.get('q', '').strip()
    products, has_related_results = _search_products(query)
    return render(request, 'catalog/search.html', {
        'query': query,
        'results': products,
        'has_related_results': has_related_results,
    })
