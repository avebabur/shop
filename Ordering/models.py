from django.contrib.auth.models import User
from django.db import models
from Product.models import Product


class Order(models.Model):
    added_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    products = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(default=1, null=True, blank=True)
