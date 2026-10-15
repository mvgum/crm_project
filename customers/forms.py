"""Формы приложения customers."""
from django import forms

from leads.models import Lead
from products.models import Product


class CustomerFromLeadForm(forms.Form):
    """Форма создания активного клиента из лида (с новым контрактом)."""

    lead = forms.ModelChoiceField(
        queryset=Lead.objects.all(),
        widget=forms.HiddenInput(),
        required=False,
    )
    name = forms.CharField(
        label='Название контракта',
        max_length=255,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    product = forms.ModelChoiceField(
        label='Услуга',
        queryset=Product.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
    )
    document = forms.FileField(
        label='Файл документа',
        widget=forms.FileInput(attrs={'class': 'form-control'}),
    )
    start_date = forms.DateField(
        label='Дата заключения',
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
    )
    end_date = forms.DateField(
        label='Дата окончания',
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
    )
    cost = forms.DecimalField(
        label='Сумма',
        max_digits=12,
        decimal_places=2,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
    )

    def __init__(self, *args, **kwargs):
        """Инициализация формы с предзаполненным лидом."""
        lead = kwargs.pop('lead', None)
        super().__init__(*args, **kwargs)
        if lead:
            self.fields['lead'].queryset = Lead.objects.filter(pk=lead.pk)
            self.fields['lead'].initial = lead
            # Предзаполняем имя контракта на основе лида
            self.fields['name'].initial = f'Контракт с {lead.full_name}'
