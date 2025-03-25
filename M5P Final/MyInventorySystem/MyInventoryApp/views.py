from django.shortcuts import render
from .models import WaterBottle, Supplier

# Create your views here.
def hello_world(request):
    return render(request, 'MyInventoryApp/hello_world.html')
def view_bottles(request): 
    bottles = WaterBottle.objects.all()
    return render(request, 'MyInventoryApp/view_bottles.html', {'bottles': bottles})
def add_bottle(request):
    return render(request, 'MyInventoryApp/add_bottle.html')
def view_suppliers(request):
    suppliers = Supplier.objects.all()
    return render(request, 'MyInventoryApp/view_suppliers.html', {'suppliers': suppliers})