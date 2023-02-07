from django.urls import path
from api.views import product, order


urlpatterns = [
    path('product/', product),
    path('order/', order)
]