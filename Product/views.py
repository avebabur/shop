from django.shortcuts import render
from Product.models import Product
from django.db.models import Q
from django.core.paginator import Paginator


def product_list(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    products = Product.objects.filter(
        Q(name__incontains=q)|
        Q(description__icontains=q)
    )
    context = {
        'products': products,
    }
    return render(request, 'Product/product_list.html', context)

def product_detail(request, slug):
    product = Product.objects.filter(slug=slug)
    context = {
        'product': product
    }
    return render(request, 'Product/product_detail.html', context)

def contact(request):
    return render(request, 'contact.html')

def shop(request):
    return render(request, 'shop.html')

def shop_single(request):
    return render(request, 'shop-single.html')
def about(request):
    return render(request, 'about.html')