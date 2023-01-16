from django.contrib import admin

# Register your models here.
from .models import Product, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    class Meta:
        model = Product

    prepopulated_fields = {"slug": ("name", )}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    class Meta:
        model = Category
