from django.shortcuts import render, redirect
from .models import Customer, FuelPurchase
from .forms import FuelPurchaseForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def index(request):
    customers = Customer.objects.all() 
    form = FuelPurchaseForm() 

    if request.method == 'POST':
        form = FuelPurchaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index') 

    return render(request, 'index.html', {
        'customers': customers,
        'form': form, 
    })

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username'] 
        password = request.POST['password'] 
        user = authenticate(request, username=username, password=password)  
        if user is not None:
            login(request, user) 
            return redirect('index') 
        else:
            return render(request, 'login.html', {'error': 'Noto‘g‘ri foydalanuvchi nomi yoki parol'})  # Xato xabari
    return render(request, 'login.html')  

@login_required 
def index(request):
    customers = Customer.objects.all() 
    form = FuelPurchaseForm()  

    if request.method == 'POST':
        form = FuelPurchaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index') 

    return render(request, 'index.html', {
        'customers': customers,
        'form': form, 
    })