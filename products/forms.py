"""Формы приложения products."""
from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    """Форма создания и редактирования услуги."""

    class Meta:
        model = Product
        fields = ['name', 'description', 'cost']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'cost': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
        }
