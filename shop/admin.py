from django.contrib import admin
from .models import Product

# Register your models here
class list_products(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'image','file')

admin.site.register(Product,list_products)


