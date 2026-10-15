"""URL-маршруты приложения customers."""
from django.urls import path

from . import views

urlpatterns = [
    path('', views.customer_list, name='customer_list'),
    path('new/', views.customer_create, name='customer_create'),
    path('new/<int:lead_pk>/', views.customer_create, name='customer_create_from_lead'),
    path('<int:pk>/', views.customer_detail, name='customer_detail'),
    path('<int:pk>/delete/', views.customer_delete, name='customer_delete'),
]
