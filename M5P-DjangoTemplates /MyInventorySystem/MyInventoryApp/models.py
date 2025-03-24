from django.db import models

# Create your models here.
class Supplier(models.Model):
    name = models.CharField(max_length=300)
    city = models.CharField(max_length=300)
    country = models.CharField(max_length=300)
    created_at = models.DateTimeField(blank=True, null=True)
    
    def getName(self):
        return self.name

    def __str__(self):
        return f"{self.name} - {self.city}, {self.country} created at: {self.created_at}"
    
class WaterBottle(models.Model):
    sku = models.CharField(max_length=100, unique=True)
    brand = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.CharField(max_length=20) # example 18oz, 1 liter
    mouth_size = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE) #refers to supplier model
    current_quantity = models.PositiveIntegerField() #number

    def __str__(self):
        return f"{self.sku}: {self.brand}, {self.mouth_size}, {self.size}, {self.color}, supplied by {self.supplier}, Cost: {self.cost}, Current Quantity: {self.current_quantity}"