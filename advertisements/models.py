"""Модели приложения advertisements."""
from django.db import models
from products.models import Product


class Advertisement(models.Model):
    """Модель рекламной кампании."""

    name = models.CharField('Название', max_length=255)
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name='Рекламируемая услуга',
    )
    channel = models.CharField('Канал продвижения', max_length=255)
    budget = models.DecimalField('Бюджет', max_digits=12, decimal_places=2)

    class Meta:
        verbose_name = 'Рекламная кампания'
        verbose_name_plural = 'Рекламные кампании'

    def __str__(self):
        return self.name

    @property
    def leads_count(self):
        """Количество лидов, привлечённых кампанией."""
        return self.lead_set.count()

    @property
    def customers_count(self):
        """Количество лидов, перешедших в активных клиентов."""
        return sum(1 for lead in self.lead_set.all() if hasattr(lead, 'customer'))

    @property
    def income(self):
        """Суммарный доход по контрактам активных клиентов кампании."""
        total = 0
        for lead in self.lead_set.all():
            if hasattr(lead, 'customer'):
                total += lead.customer.contract.cost
        return total

    @property
    def profit(self):
        """Соотношение дохода к затратам на рекламу."""
        if self.budget and self.budget > 0:
            return round(self.income / self.budget, 2)
        return None
