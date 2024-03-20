from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext as _

from .models import Connection

class ConnectionRequestForm(forms.ModelForm):
    class Meta:
        model = Connection
        fields = []

class ConnectionAcceptForm(forms.ModelForm):
    class Meta:
        model = Connection
        fields = []

class ConnectionRejectForm(forms.ModelForm):
    class Meta:
        model = Connection
        fields = []

# Доданий клас форми для реєстрації користувача
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(label=_("Email"), required=True)
    password1 = forms.CharField(label=_("Password"), strip=False, widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(label=_("Password confirmation"), widget=forms.PasswordInput, strip=False, required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="Email", required=True)
    password1 = forms.CharField(label="Password", strip=False, widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(label="Password confirmation", widget=forms.PasswordInput, strip=False, required=True)

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')