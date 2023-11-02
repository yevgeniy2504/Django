from django.contrib import admin
from .models import Category, Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'image', 'is_delete']
    list_filter = ['price', 'name']
    fields = [
        ('name', 'category'),
        ('price', 'stock'),
        ('discount', 'image'),
    ]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'is_delete']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
