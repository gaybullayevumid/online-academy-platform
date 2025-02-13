from django.contrib import admin
from .models import Customer, FuelPurchase

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone_number', 'address', 'total_points')

@admin.register(FuelPurchase)
class FuelPurchaseAdmin(admin.ModelAdmin):
    list_display = ('customer', 'petrol_type', 'litres', 'get_customer_points')

    def get_customer_points(self, obj):
        return obj.customer.total_points
    get_customer_points.short_description = 'Total Points'