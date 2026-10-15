"""Главное представление — общая статистика."""
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from advertisements.models import Advertisement
from customers.models import Customer
from leads.models import Lead
from products.models import Product


@login_required
def index(request):
    """Главная страница с общей статистикой."""
    context = {
        'products_count': Product.objects.count(),
        'advertisements_count': Advertisement.objects.count(),
        'leads_count': Lead.objects.count(),
        'customers_count': Customer.objects.count(),
    }
    return render(request, 'index.html', context)
