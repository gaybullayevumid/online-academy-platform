# Online Academy Platform

online_academy/
├── backend/                # Django REST qismi
│   ├── academy/            # Main project config (settings, urls, wsgi, asgi)
│   ├── apps/               # Modular structure (har bir funksiya alohida app)
│   │   ├── accounts/       # Autentifikatsiya, Custom User
│   │   ├── courses/        # Kurslar va darslar
│   │   ├── lessons/        # Darslar (video, file, matn)
│   │   ├── quizzes/        # Testlar (MCQ, yozma)
│   │   ├── certificates/   # Sertifikat generatsiya (PDF export)
│   │   ├── payments/       # To‘lov tizimi (Stripe, Payme, Click integratsiya)
│   │   ├── feedback/       # Kurslarga izoh va reyting
│   │   ├── notifications/  # Email / Telegram bot xabarnomalari
│   │   └── dashboard/      # Statistikalar (Admin & Teacher uchun)
│   ├── media/              # Yuklangan fayllar (video, pdf va h.k.)
│   ├── static/             # Statik fayllar
│   ├── requirements.txt    # Django dependencies
│   └── manage.py
│
├── frontend/               # Vue.js qismi
│   ├── public/             # Favicon, index.html
│   ├── src/
│   │   ├── assets/         # Rasm, ikonka, umumiy style
│   │   ├── components/     # Qayta foydalaniladigan Vue komponentlar
│   │   │   ├── Navbar.vue
│   │   │   ├── Footer.vue
│   │   │   ├── CourseCard.vue
│   │   │   └── ProgressBar.vue
│   │   ├── layouts/        # Layouts (MainLayout, AdminLayout)
│   │   ├── pages/          # Asosiy sahifalar
│   │   │   ├── Home.vue
│   │   │   ├── Courses.vue
│   │   │   ├── CourseDetail.vue
│   │   │   ├── Quiz.vue
│   │   │   ├── Profile.vue
│   │   │   ├── Dashboard.vue
│   │   │   └── LoginRegister.vue
│   │   ├── router/         # Vue Router konfiguratsiya
│   │   │   └── index.js
│   │   ├── store/          # Pinia/Vuex holat boshqaruvi
│   │   │   └── user.js
│   │   │   └── courses.js
│   │   ├── services/       # API bilan ishlash (axios instance)
│   │   │   ├── api.js
│   │   │   └── auth.js
│   │   └── App.vue
│   └── package.json
│
├── docker-compose.yml      # Agar Docker ishlatsangiz
├── .env                    # Environment variables
└── README.md
