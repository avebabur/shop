from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from Product.models import Product
from Product.forms import ProductForm


def sign_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('product_list')
        else:
            messages.error(request, 'Username or password is incorrect')
    context = {}
    return render(request, 'registration/sign_in.html', context)

def sign_out(request):
    logout(request)
    return redirect('product_list')

def sign_up(request):
    form = UserCreationForm
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request, user)
            return redirect('product_list')
        else:
            messages.error(request, 'An error occured during registration')
    context = {
        'form': form
    }
    return render(request, 'registration/sign_up.html', context)

def my_products(request):
    products = Product.objects.filter(author=request.user.id)
    context = {
        'products': products
    }
    return render(request, 'Customer/my_products.html', context)

def product_create(request):
    form = ProductForm
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.author = request.user
            user.save()
        else:
            messages.error(request, 'An error occured during creating the listing')
    context = {
        'form': form
    }

    return render(request, 'Customer/product_create.html', context)