from django.contrib import admin
from .models import Product, ProductViews

class ProductAdmin(admin.ModelAdmin):
    list_display = ["title", "product_type"]
    list_filter = ["product_type"]

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductViews)
