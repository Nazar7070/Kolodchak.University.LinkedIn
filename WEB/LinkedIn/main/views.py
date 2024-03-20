from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Connection
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignUpForm, CustomUserCreationForm


def index(request):
    return render(request, 'LinkedIn/index.html')


def about(request):
    return render(request, 'LinkedIn/about.html')


def home(request):
    return render(request, 'LinkedIn/home.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Перенаправлення на головну сторінку після успішної реєстрації
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


class SignUpView(View):
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('home'))  # Перенаправлення на головну сторінку після успішної реєстрації
        return render(request, 'signup.html', {'form': form})  # Відображення форми реєстрації з повідомленням про помилку


@login_required
def send_connection_request(request, receiver_id):
    receiver = get_object_or_404(User, pk=receiver_id)
    if request.method == 'POST':
        Connection.objects.create(sender=request.user, receiver=receiver)
        messages.success(request, f"Connection request sent to {receiver.username}")
        return redirect('my_network')  # Перенаправлення на сторінку "Моя мережа" після відправлення запиту на з'єднання
    return render(request, 'send_connection_request.html', {'receiver': receiver})

@login_required
def accept_connection_request(request, connection_id):
    connection = get_object_or_404(Connection, pk=connection_id)
    if request.method == 'POST':
        connection.status = 'accepted'
        connection.save()
        messages.success(request, "Connection request accepted")
        return redirect('my_network')  # Перенаправлення на сторінку "Моя мережа" після підтвердження запиту на з'єднання
    return render(request, 'accept_connection_request.html', {'connection': connection})

@login_required
def reject_connection_request(request, connection_id):
    connection = get_object_or_404(Connection, pk=connection_id)
    if request.method == 'POST':
        connection.status = 'rejected'
        connection.save()
        messages.success(request, "Connection request rejected")
        return redirect('my_network')  # Перенаправлення на сторінку "Моя мережа" після відмови від запиту на з'єднання
    return render(request, 'reject_connection_request.html', {'connection': connection})

@login_required
def my_network(request):
    connections_sent = request.user.sent_connections.all()
    connections_received = request.user.received_connections.all()
    return render(request, 'my_network.html', {'connections_sent': connections_sent, 'connections_received': connections_received})

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            # Обробка валідних даних форми
            # Отримання очищених даних
            email = form.cleaned_data['email']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            # Тут можна зробити що завгодно з цими даними, наприклад, створити нового користувача
            # user = form.save()  # Зберегти користувача в базі даних
            # Після успішного збереження можна перенаправити користувача або відобразити повідомлення про успішну реєстрацію
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
