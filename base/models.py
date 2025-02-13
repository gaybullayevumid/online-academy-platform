from django.db import models
import random

PETROL_TYPES = [
        (80, '80'),
        (91, '91'),
        (92, '92'),
        (95, '95'),
    ]


class Customer(models.Model):
    unique_id = models.CharField(max_length=7, 
                                 unique=True, 
                                 editable=False, 
                                 verbose_name='Foydalanuvchi ID')
    phone_number = models.CharField(max_length=15, verbose_name='Telefon raqam')
    full_name = models.CharField(max_length=100, verbose_name='Foydalanuvchi ismi')
    address = models.TextField(verbose_name='Manzil')
    total_points = models.FloatField(default=0, verbose_name='Jami ballar')

    def save(self, *args, **kwargs):
        if not self.unique_id:
            self.unique_id = self.generate_unique_id_customer()
        super().save(*args, **kwargs)

    def generate_unique_id_customer(self):
        while True:
            unique_id = ''.join(random.choices('0123456789', k=7))
            if not Customer.objects.filter(unique_id=unique_id).exists():
                return unique_id

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