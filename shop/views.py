from django.shortcuts import render
from django.core.paginator import Paginator
from shop.models import Product

def get_data(request):
    # Fetch all products
    all_products = Product.objects.all()

    # Number of items per page
    items_per_page = 10

    # Initialize the paginator with the fetched data and the number of items per page
    paginator = Paginator(all_products, items_per_page)

    # Get the current page number from the request, default to 1 if not provided
    page_number = request.GET.get('page', 1)

    # Get the products for the requested page
    data = paginator.get_page(page_number)

    return render(request, 'product.html', {'page_obj': data})
