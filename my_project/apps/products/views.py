from django.shortcuts import render
from .models import Product
from .services import get_product_details


def products(request):
    return render(
        request,
        'products/list.html',
        {
            'products': Product.objects.all().values(),
        }
    )

def product(request, id):
    return render(
        request,
        'products/detail.html',
        {
            'product': get_product_details(Product.objects.get(id=id)),
        }
    )