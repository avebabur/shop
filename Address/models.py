from django.db import models
from django.contrib.auth.models import User
from Ordering.models import Order
from Product.models import Product


class ShippingAddress(models.Model):
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.PROTECT, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.PROTECT, blank=True, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)