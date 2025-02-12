# fuel_app/models.py

from django.db import models

class Customer(models.Model):
    phone_number = models.CharField(max_length=15)
    full_name = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return self.full_name

class FuelPurchase(models.Model):
    PETROL_TYPES = [
        (80, '80'),
        (91, '91'),
        (92, '92'),
        (95, '95'),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    petrol_type = models.IntegerField(choices=PETROL_TYPES)
    litres = models.FloatField()
    total_points = models.FloatField(editable=False)

    def save(self, *args, **kwargs):
        if self.petrol_type == 80:
            self.total_points = self.litres * 0.1
        elif self.petrol_type in [91, 92]:
            self.total_points = self.litres * 0.2
        elif self.petrol_type == 95:
            self.total_points = self.litres * 0.3
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.customer.full_name} - {self.petrol_type}"