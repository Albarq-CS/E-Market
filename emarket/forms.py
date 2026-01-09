from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['prodName', 'Price', 'Suppliers', 'Category', 'Quantity', 'image']
        widgets = {
            'prodName': forms.TextInput(attrs={'class': 'form-control'}),
            'Price': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'Suppliers': forms.Select(attrs={'class': 'form-select'}),
            'Category': forms.Select(attrs={'class': 'form-select'}),
            'Quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }
