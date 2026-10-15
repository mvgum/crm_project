"""Формы приложения leads."""
from django import forms

from .models import Lead


class LeadForm(forms.ModelForm):
    """Форма создания и редактирования лида."""

    class Meta:
        model = Lead
        fields = ['last_name', 'first_name', 'middle_name', 'phone', 'email', 'advertisement']
        widgets = {
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'middle_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'advertisement': forms.Select(attrs={'class': 'form-control'}),
        }
