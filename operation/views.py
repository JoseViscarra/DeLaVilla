from django.shortcuts import render

# Create your views here.

def dashboard(request):
    return render(request, 'operation/dashboard.html')

def production(request):
    return render(request, 'operation/production.html')

def orders(request):
    return render(request, 'operation/orders.html')

def customer(request):
    return render(request, 'operation/customer.html')