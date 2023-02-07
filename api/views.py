from django.shortcuts import render
from django.http import JsonResponse
from Product.models import Product
from Address.models import ShippingAddress
from Ordering.models import Order
from django.contrib.auth.models import User
from .serializers import OrderSerializer, ProductSerializer, UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def order(request):
    order = Order.objects.all()
    serializer = OrderSerializer(order, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def product(request):
    product = Product.objects.all()
    serializer = ProductSerializer(product, many=True)
    return Response(serializer.data)
"""
@api_view(['GET'])
def user(request):
    user = User.objects.all()
    serializer = UserSerializer(Product, many=True)"""