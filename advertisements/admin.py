"""Настройка админки для приложения advertisements."""
from django.contrib import admin
from .models import Advertisement


@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    """Отображение рекламных кампаний в админке."""

    list_display = ('id', 'name', 'product', 'channel', 'budget')
    list_filter = ('channel', 'product')
    search_fields = ('name',)
    ordering = ('id',)
