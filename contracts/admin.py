"""Настройка админки для приложения contracts."""
from django.contrib import admin
from .models import Contract


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    """Отображение контрактов в админке."""

    list_display = ('id', 'name', 'product', 'start_date', 'end_date', 'cost')
    list_filter = ('product',)
    search_fields = ('name',)
    ordering = ('id',)
