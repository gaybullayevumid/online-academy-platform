from django.db import models

class Nfc(models.Model):
    phone = models.CharField(max_length=13)
    address = models.CharField(max_length=255)
    score = models.FloatField()  # Ballni saqlash uchun
    petrol_type = models.CharField(max_length=10)  # Petrol turi (80, 91/92, 95)

    def __str__(self):
        return f"{self.phone} - {self.score} ({self.petrol_type})"
