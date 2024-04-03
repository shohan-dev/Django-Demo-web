from django.shortcuts import render
from shop.models import *


# Create your views here.

def get_data(request):
    data = Product.objects.all()
    return render(request, 'product.html', {'data': data})