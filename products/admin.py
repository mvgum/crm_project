"""Настройка админки для приложения products."""
from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Отображение услуг в админке."""

    list_display = ('id', 'name', 'cost')
    search_fields = ('name',)
    ordering = ('id',)
