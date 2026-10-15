"""URL-маршруты приложения advertisements."""
from django.urls import path

from . import views

urlpatterns = [
    path('', views.ad_list, name='ad_list'),
    path('new/', views.ad_create, name='ad_create'),
    path('statistic/', views.ad_statistic, name='ad_statistic'),
    path('<int:pk>/', views.ad_detail, name='ad_detail'),
    path('<int:pk>/edit/', views.ad_edit, name='ad_edit'),
    path('<int:pk>/delete/', views.ad_delete, name='ad_delete'),
]
