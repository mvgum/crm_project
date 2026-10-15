"""Формы приложения contracts."""
from django import forms

from .models import Contract


class ContractForm(forms.ModelForm):
    """Форма создания и редактирования контракта."""

    class Meta:
        model = Contract
        fields = ['name', 'product', 'document', 'start_date', 'end_date', 'cost']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'product': forms.Select(attrs={'class': 'form-control'}),
            'document': forms.FileInput(attrs={'class': 'form-control'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'cost': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
        }
