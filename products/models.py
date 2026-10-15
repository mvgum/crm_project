"""Модели приложения products."""
from django.db import models


class Product(models.Model):
    """Модель услуги, предоставляемой компанией."""

    name = models.CharField('Название', max_length=255)
    description = models.TextField('Описание')
    cost = models.DecimalField('Стоимость', max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    def __str__(self):
        return self.name
