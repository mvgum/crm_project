"""Представления приложения contracts."""
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ContractForm
from .models import Contract


@login_required
@permission_required('contracts.view_contract', raise_exception=True)
def contract_list(request):
    """Список контрактов."""
    contracts = Contract.objects.all()
    return render(request, 'contracts-list.html', {'contracts': contracts})


@login_required
@permission_required('contracts.view_contract', raise_exception=True)
def contract_detail(request, pk):
    """Детальная страница контракта."""
    contract = get_object_or_404(Contract, pk=pk)
    return render(request, 'contracts-detail.html', {'object': contract})


@login_required
@permission_required('contracts.add_contract', raise_exception=True)
def contract_create(request):
    """Создание контракта."""
    if request.method == 'POST':
        form = ContractForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('contract_list')
    else:
        form = ContractForm()
    return render(request, 'contracts-create.html', {'form': form})


@login_required
@permission_required('contracts.change_contract', raise_exception=True)
def contract_edit(request, pk):
    """Редактирование контракта."""
    contract = get_object_or_404(Contract, pk=pk)
    if request.method == 'POST':
        form = ContractForm(request.POST, request.FILES, instance=contract)
        if form.is_valid():
            form.save()
            return redirect('contract_detail', pk=contract.pk)
    else:
        form = ContractForm(instance=contract)
    return render(request, 'contracts-edit.html', {'form': form, 'object': contract})


@login_required
@permission_required('contracts.delete_contract', raise_exception=True)
def contract_delete(request, pk):
    """Удаление контракта."""
    contract = get_object_or_404(Contract, pk=pk)
    if request.method == 'POST':
        contract.delete()
        return redirect('contract_list')
    return render(request, 'contracts-delete.html', {'object': contract})

