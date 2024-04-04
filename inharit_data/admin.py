from django.contrib import admin
from .models import  Test_Product_1, Test_Product_2


class TestProduct1Admin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'discount', 'description')

admin.site.register(Test_Product_1, TestProduct1Admin)

class TestProduct2Admin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'quantity', 'add_cart', 'discount', 'description')

admin.site.register(Test_Product_2, TestProduct2Admin)
