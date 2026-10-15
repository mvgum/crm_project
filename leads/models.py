"""Модели приложения leads."""
from django.db import models
from advertisements.models import Advertisement


class Lead(models.Model):
    """Модель потенциального клиента (лида)."""

    last_name = models.CharField('Фамилия', max_length=100)
    first_name = models.CharField('Имя', max_length=100)
    middle_name = models.CharField('Отчество', max_length=100, blank=True)
    phone = models.CharField('Телефон', max_length=20)
    email = models.EmailField('Email')
    advertisement = models.ForeignKey(
        Advertisement,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Рекламная кампания',
    )

    class Meta:
        verbose_name = 'Потенциальный клиент'
        verbose_name_plural = 'Потенциальные клиенты'

    def __str__(self):
        return f'{self.last_name} {self.first_name}'

    @property
    def full_name(self):
        """Полное Ф. И. О."""
        return f'{self.last_name} {self.first_name} {self.middle_name}'.strip()
