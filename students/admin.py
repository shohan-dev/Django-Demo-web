from django.contrib import admin
from .models import *

# # Register your models here.

class list_products(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'discount','description')

admin.site.register(Test_Product,list_products)
