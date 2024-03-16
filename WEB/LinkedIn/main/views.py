from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse


def index(request):
    return render(request, 'LinkedIn/index.html')


def about(request):
    return render(request, 'LinkedIn/about.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Перенаправлення на головну сторінку після успішної реєстрації
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def home(request):
    return render(request, 'LinkedIn/home.html')


class SignUpView(View):
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('home'))  # Перенаправлення на головну сторінку після успішної реєстрації
        return render(request, 'signup.html', {'form': form})  # Відображення форми реєстрації з повідомленням про помилку
