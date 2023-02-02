from django.urls import path
from .views import product_list, product_detail, shop, shop_single, contact,about


urlpatterns = [
    path('', product_list, name='product_list'),
    path('<slug:slug>/', product_detail, name='product_detail'),
    path('contact/', contact, name='contact'),
    path('shop_single/', shop_single, name='shop_single'),
    path('about/', about, name='about')
]