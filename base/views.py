# fuel_app/views.py

from django.shortcuts import render, redirect
from .models import Customer, FuelPurchase
from .forms import FuelPurchaseForm

def index(request):
    customers = Customer.objects.all()  # Barcha mijozlarni olish
    form = FuelPurchaseForm()  # Yoqilg'i sotib olish formasi

    if request.method == 'POST':
        form = FuelPurchaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Ma'lumot saqlangandan so'ng sahifani yangilash

    return render(request, 'index.html', {
        'customers': customers,
        'form': form,  # Formani templatega uzatish
    })