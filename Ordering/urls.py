from django.urls import path
from .views import addtocart, cart


urlpatterns = [
    path('addtocart/<slug:slug>/', addtocart, name='addtocart'),
    path('cart/', cart, name='cart')
]