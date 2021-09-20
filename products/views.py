from django.shortcuts import render
from .models import Product

# Create your views here.


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()

    context = {
        'products': products,
        # 'search_term': query,
        # 'current_categories': categories,
        # 'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)