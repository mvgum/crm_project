"""Корневые URL-маршруты проекта."""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from .views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', index, name='index'),
    path('products/', include('products.urls')),
    path('ads/', include('advertisements.urls')),
    path('leads/', include('leads.urls')),
    path('contracts/', include('contracts.urls')),
    path('customers/', include('customers.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
