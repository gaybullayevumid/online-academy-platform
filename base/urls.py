# fuel_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('purchase/', views.purchase_fuel, name='purchase_fuel'),
]