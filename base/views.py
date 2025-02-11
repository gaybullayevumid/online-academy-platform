from django.shortcuts import render, redirect
from .models import Nfc

def home(request):
    if request.method == 'POST':
        # Foydalanuvchidan kiritilgan telefon raqamini olish
        phone = request.POST.get('phone')
        
        if not phone:
            # Agar telefon raqami bo'lmasa, xato xabarini ko'rsatish
            return render(request, 'base.html', {'error': 'Telefon raqami kiritilishi kerak!'})

        input_number = request.POST.get('input_number')
        petrol_type = request.POST.get('petrol_type')

        # Petrol turiga qarab multiplikatorni aniqlash
        if petrol_type == '80':
            multiplier = 0.1
        elif petrol_type in ['91', '92']:
            multiplier = 0.2
        elif petrol_type == '95':
            multiplier = 0.3
        else:
            multiplier = 0.1  # Standart qiymat

        # Hisoblangan ball
        score = float(input_number) * multiplier

        # Foydalanuvchining phone raqami bilan mavjud Nfc obyektini topish
        nfc = Nfc.objects.filter(phone=phone).first()

        if nfc:
            # Agar foydalanuvchi mavjud bo'lsa, eski ballni qo'shish
            new_score = nfc.score + score
            nfc.score = new_score  # Yangilangan score
            nfc.save()  # Ma'lumotni saqlash
        else:
            # Yangi foydalanuvchi yaratish
            nfc_entry = Nfc(phone=phone, address=request.POST.get('address'), score=score, petrol_type=petrol_type)
            nfc_entry.save()

        # Saqlashdan keyin muvaffaqiyatli sahifaga yo'naltirish
        return redirect('success_page')  # Bu yerda 'success_page' - saqlash muvaffaqiyatli bo'lgan sahifa nomi

    return render(request, 'pages/home.html')



def success(request):
    return render(request, 'pages/succes.html')
