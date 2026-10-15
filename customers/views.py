"""Представления приложения customers."""
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import get_object_or_404, redirect, render

from contracts.models import Contract
from leads.models import Lead
from .forms import CustomerFromLeadForm
from .models import Customer


@login_required
@permission_required('customers.view_customer', raise_exception=True)
def customer_list(request):
    """Список активных клиентов."""
    customers = Customer.objects.all()
    return render(request, 'customers-list.html', {'customers': customers})


@login_required
@permission_required('customers.view_customer', raise_exception=True)
def customer_detail(request, pk):
    """Детальная страница активного клиента."""
    customer = get_object_or_404(Customer, pk=pk)
    return render(request, 'customers-detail.html', {'object': customer})


@login_required
@permission_required('customers.add_customer', raise_exception=True)
def customer_create(request, lead_pk=None):
    """Создание активного клиента из лида."""
    lead = None
    if lead_pk:
        lead = get_object_or_404(Lead, pk=lead_pk)

    if request.method == 'POST':
        form = CustomerFromLeadForm(request.POST, request.FILES, lead=lead)
        if form.is_valid():
            contract = Contract.objects.create(
                name=form.cleaned_data['name'],
                product=form.cleaned_data['product'],
                document=form.cleaned_data['document'],
                start_date=form.cleaned_data['start_date'],
                end_date=form.cleaned_data['end_date'],
                cost=form.cleaned_data['cost'],
            )
            Customer.objects.create(lead=lead, contract=contract)
            return redirect('customer_list')
    else:
        form = CustomerFromLeadForm(lead=lead)
    return render(request, 'customers-create.html', {'form': form, 'lead': lead})


@login_required
@permission_required('customers.delete_customer', raise_exception=True)
def customer_delete(request, pk):
    """Удаление активного клиента."""
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        customer.delete()
        return redirect('customer_list')
    return render(request, 'customers-delete.html', {'object': customer})

