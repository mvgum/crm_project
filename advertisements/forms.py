"""Формы приложения advertisements."""
from django import forms

from .models import Advertisement


class AdvertisementForm(forms.ModelForm):
    """Форма создания и редактирования рекламной кампании."""

    class Meta:
        model = Advertisement
        fields = ['name', 'product', 'channel', 'budget']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'product': forms.Select(attrs={'class': 'form-control'}),
            'channel': forms.TextInput(attrs={'class': 'form-control'}),
            'budget': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
        }
