from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['costumer_name', 'costumer_email', 'costumer_mobile',]
