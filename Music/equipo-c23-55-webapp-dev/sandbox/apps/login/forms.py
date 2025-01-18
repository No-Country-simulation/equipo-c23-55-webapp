from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=150)
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'password']
