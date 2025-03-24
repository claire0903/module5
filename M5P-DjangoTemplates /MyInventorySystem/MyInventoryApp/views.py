from django.shortcuts import render
from .models import WaterBottle, Supplier

def hello_world(request):
    return render(request, 'MyInventoryApp/hello_world.html')

def view_bottles(request): 
    bottles = WaterBottle.objects.all()
    return render(request, 'view_bottles.html', {'bottles': bottles})

def add_bottle(request):
    return render(request, 'add_bottle.html')

def view_supplier(request): 
    suppliers = Supplier.objects.all()
    return render(request, 'view_suppliers.html', {'suppliers': suppliers})
