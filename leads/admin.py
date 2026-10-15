"""Настройка админки для приложения leads."""
from django.contrib import admin
from .models import Lead


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    """Отображение лидов в админке."""

    list_display = ('id', 'last_name', 'first_name', 'phone', 'email', 'advertisement')
    list_filter = ('advertisement',)
    search_fields = ('last_name', 'first_name', 'phone', 'email')
    ordering = ('id',)
