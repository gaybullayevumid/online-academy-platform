from django.contrib import admin
from .models import Nfc

class NfcAdmin(admin.ModelAdmin):
    list_display = ('phone', 'address', 'score', 'petrol_type')  # Admin panelida ko'rsatiladigan ustunlar
    search_fields = ('phone', 'address')  # Telefon va manzil bo'yicha qidirish

admin.site.register(Nfc, NfcAdmin)
