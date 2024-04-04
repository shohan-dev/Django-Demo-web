from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'image', 'file')

admin.site.register(Product, ProductAdmin)


