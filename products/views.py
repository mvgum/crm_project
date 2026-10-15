"""Представления приложения products."""
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ProductForm
from .models import Product


@login_required
@permission_required('products.view_product', raise_exception=True)
def product_list(request):
    """Список услуг."""
    products = Product.objects.all()
    return render(request, 'products-list.html', {'products': products})


@login_required
@permission_required('products.view_product', raise_exception=True)
def product_detail(request, pk):
    """Детальная страница услуги."""
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products-detail.html', {'object': product})


@login_required
@permission_required('products.add_product', raise_exception=True)
def product_create(request):
    """Создание услуги."""
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'products-create.html', {'form': form})


@login_required
@permission_required('products.change_product', raise_exception=True)
def product_edit(request, pk):
    """Редактирование услуги."""
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_detail', pk=product.pk)
    else:
        form = ProductForm(instance=product)
    return render(request, 'products-edit.html', {'form': form, 'object': product})


@login_required
@permission_required('products.delete_product', raise_exception=True)
def product_delete(request, pk):
    """Удаление услуги."""
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'products-delete.html', {'object': product})

