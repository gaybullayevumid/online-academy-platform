# fuel_app/admin.py

from django.contrib import admin
from .models import Customer, FuelPurchase

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone_number', 'address')

@admin.register(FuelPurchase)
class FuelPurchaseAdmin(admin.ModelAdmin):
    list_display = ('customer', 'petrol_type', 'litres', 'total_points')