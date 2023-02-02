from django.shortcuts import render, redirect
from .forms import ShippingAddressForm


def buy(request):
    form = ShippingAddressForm
    if request.method == 'POST':
        form = ShippingAddressForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    context = {
        'form': form
    }
    return render(request, 'Address/buy.html', context)