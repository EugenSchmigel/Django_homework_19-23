from django.contrib import admin

from catalog.models import Product, Category, Version


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk','name','price', 'category', 'user', 'is_published')

    list_filter = ('category', )
    search_fields = ('name', 'description')


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('pk','version_number','version_name', 'is_active', 'product')

    list_filter = ('version_number', )
    search_fields = ('product', 'version_number',)


@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display = ('pk', 'name', )

