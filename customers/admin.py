"""Настройка админки для приложения customers."""
from django.contrib import admin
from .models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    """Отображение активных клиентов в админке."""

    list_display = ('id', 'lead', 'contract')
    search_fields = ('lead__last_name', 'lead__first_name')
    ordering = ('id',)
