from django.shortcuts import render
from .forms import OrderForm
from django.contrib import messages
from Ordering.models import Order
from Product.models import Product


def addtocart(request, slug):
    form = OrderForm
    if request.method == 'POST':
        form = OrderForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.added_by = request.user
            obj.products = Product.objects.get(slug=slug)
            obj.save()
        else:
            messages.error(request, 'An error occured during creating the listing')
    context = {
        'form': form
    }

    return render(request, 'Ordering/addtocart.html', context)

def cart(request):
    products = Order.objects.filter(author=request.user)
    context = {
        'products': products
    }
    
    return render(request, 'Ordering/cart.html', context)
