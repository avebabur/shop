from django.urls import path
from .views import sign_up, sign_in, sign_out, my_products, product_create


urlpatterns = [
    path('sign_in/', sign_in, name='sign_in'),
    path('sign_up/', sign_up, name='sign_up'),
    path('sign_out/', sign_out, name='sign_out'),
    path('my_products/', my_products, name='my_products'),
    path('product_create/', product_create, name='product_create')
]