# fuel_app/views.py

from django.shortcuts import render, redirect
from .models import Customer, FuelPurchase
from .forms import FuelPurchaseForm

def index(request):
    customers = Customer.objects.all()
    return render(request, 'index.html', {
        'customers': customers,
    })

def purchase_fuel(request):
    if request.method == 'POST':
        form = FuelPurchaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = FuelPurchaseForm()
    return render(request, 'purchase_fuel.html', {'form': form})