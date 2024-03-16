from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about-us/', views.about),
    path('home/', views.home, name='home'),  # Додано URL-адресу для сторінки "/home"
    path('signup/', views.signup, name='signup'),
]
