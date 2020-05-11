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
            'description',
            'tag'
        ]

        widgets = {
            'customer': forms.TextInput(attrs={'class': 'form_field form_input'}),
            'phone': forms.TextInput(attrs={'class': 'form_field form_input phone_field'}),
            'email': forms.TextInput(attrs={'class': 'form_field form_input'}),
            'adress': forms.TextInput(attrs={'class': 'form_field form_input'}),
            'description': forms.Textarea(attrs={'class': 'form_field form_area'}),
        }


class OrderUpdateForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ['tag']
