from django.forms import ModelForm
from .models import Product, Comments

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'inStock', 'image', 'rubric', 'slug']

