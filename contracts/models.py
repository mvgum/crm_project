"""Модели приложения contracts."""
from django.db import models
from products.models import Product


class Contract(models.Model):
    """Модель контракта с клиентом."""

    name = models.CharField('Название', max_length=255)
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name='Предоставляемая услуга',
    )
    document = models.FileField('Файл документа', upload_to='contracts/')
    start_date = models.DateField('Дата заключения')
    end_date = models.DateField('Дата окончания')
    cost = models.DecimalField('Сумма', max_digits=12, decimal_places=2)

    class Meta:
        verbose_name = 'Контракт'
        verbose_name_plural = 'Контракты'

    def __str__(self):
        return self.name
