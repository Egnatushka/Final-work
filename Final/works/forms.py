from django import forms
from .models import *


class OrderForm(forms.ModelForm):
    
    class Meta:
        model = Order
        fields = [
            'customer',
            'phone',
            'email',
            'adress',
            'description'
        ]


class OrderUpdateForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ['tag']