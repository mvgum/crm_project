"""Представления приложения leads."""
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import LeadForm
from .models import Lead


@login_required
@permission_required('leads.view_lead', raise_exception=True)
def lead_list(request):
    """Список потенциальных клиентов."""
    leads = Lead.objects.all()
    return render(request, 'leads-list.html', {'leads': leads})


@login_required
@permission_required('leads.view_lead', raise_exception=True)
def lead_detail(request, pk):
    """Детальная страница лида."""
    lead = get_object_or_404(Lead, pk=pk)
    return render(request, 'leads-detail.html', {'object': lead})


@login_required
@permission_required('leads.add_lead', raise_exception=True)
def lead_create(request):
    """Создание лида."""
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lead_list')
    else:
        form = LeadForm()
    return render(request, 'leads-create.html', {'form': form})


@login_required
@permission_required('leads.change_lead', raise_exception=True)
def lead_edit(request, pk):
    """Редактирование лида."""
    lead = get_object_or_404(Lead, pk=pk)
    if request.method == 'POST':
        form = LeadForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            return redirect('lead_detail', pk=lead.pk)
    else:
        form = LeadForm(instance=lead)
    return render(request, 'leads-edit.html', {'form': form, 'object': lead})


@login_required
@permission_required('leads.delete_lead', raise_exception=True)
def lead_delete(request, pk):
    """Удаление лида."""
    lead = get_object_or_404(Lead, pk=pk)
    if request.method == 'POST':
        lead.delete()
        return redirect('lead_list')
    return render(request, 'leads-delete.html', {'object': lead})

