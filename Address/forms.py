from Address.models import ShippingAddress
from django.forms import ModelForm


class ShippingAddressForm(ModelForm):
    class Meta:
        model = ShippingAddress
        fields = '__all__'