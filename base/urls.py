from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home view
    path('success/', views.success, name='success_page'),  # Success sahifasi
]
