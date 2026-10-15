"""Представления приложения advertisements."""
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import AdvertisementForm
from .models import Advertisement


@login_required
@permission_required('advertisements.view_advertisement', raise_exception=True)
def ad_list(request):
    """Список рекламных кампаний."""
    ads = Advertisement.objects.all()
    return render(request, 'ads-list.html', {'ads': ads})


@login_required
@permission_required('advertisements.view_advertisement', raise_exception=True)
def ad_detail(request, pk):
    """Детальная страница рекламной кампании."""
    ad = get_object_or_404(Advertisement, pk=pk)
    return render(request, 'ads-detail.html', {'object': ad})


@login_required
@permission_required('advertisements.add_advertisement', raise_exception=True)
def ad_create(request):
    """Создание рекламной кампании."""
    if request.method == 'POST':
        form = AdvertisementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ad_list')
    else:
        form = AdvertisementForm()
    return render(request, 'ads-create.html', {'form': form})


@login_required
@permission_required('advertisements.change_advertisement', raise_exception=True)
def ad_edit(request, pk):
    """Редактирование рекламной кампании."""
    ad = get_object_or_404(Advertisement, pk=pk)
    if request.method == 'POST':
        form = AdvertisementForm(request.POST, instance=ad)
        if form.is_valid():
            form.save()
            return redirect('ad_detail', pk=ad.pk)
    else:
        form = AdvertisementForm(instance=ad)
    return render(request, 'ads-edit.html', {'form': form, 'object': ad})


@login_required
@permission_required('advertisements.delete_advertisement', raise_exception=True)
def ad_delete(request, pk):
    """Удаление рекламной кампании."""
    ad = get_object_or_404(Advertisement, pk=pk)
    if request.method == 'POST':
        ad.delete()
        return redirect('ad_list')
    return render(request, 'ads-delete.html', {'object': ad})


@login_required
@permission_required('advertisements.view_advertisement', raise_exception=True)
def ad_statistic(request):
    """Статистика рекламных кампаний."""
    ads = Advertisement.objects.all()
    return render(request, 'ads-statistic.html', {'ads': ads})

