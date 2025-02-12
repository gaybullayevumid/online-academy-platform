# fuel_app/forms.py

from django import forms
from .models import FuelPurchase

class FuelPurchaseForm(forms.ModelForm):
    class Meta:
        model = FuelPurchase
        fields = ['customer', 'petrol_type', 'litres']