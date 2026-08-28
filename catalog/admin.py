from django.contrib import admin
from .models import Category, Product

# Register your models here.

admin.site.register(Category)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'category', 'quantity', 'price')  # since you just added slug to __str__/display
    search_fields = ('name', 'slug')
    list_filter = ('category',)