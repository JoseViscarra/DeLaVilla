from django.shortcuts import render

# Create your views here.

def operation_main(request):
    return render(request, 'operation/operationmain.html' )

def customer(request):
    return render(request, 'operation/customer.html')