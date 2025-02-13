from django.db import models


PETROL_TYPES = [
        (80, '80'),
        (91, '91'),
        (92, '92'),
        (95, '95'),
    ]


class Customer(models.Model):
    phone_number = models.CharField(max_length=15)
    full_name = models.CharField(max_length=100)
    address = models.TextField()
    total_points = models.FloatField(default=0)

    def __str__(self):
        return self.full_name

class FuelPurchase(models.Model):
    

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    petrol_type = models.IntegerField(choices=PETROL_TYPES)
    litres = models.FloatField()

    def save(self, *args, **kwargs):
        if self.petrol_type == 80:
            points = self.litres * 0.1
        elif self.petrol_type in [91, 92]:
            points = self.litres * 0.2
        elif self.petrol_type == 95:
            points = self.litres * 0.3
        else:
            points = 0

        self.customer.total_points += points
        self.customer.save()

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.customer.full_name} - {self.petrol_type}"