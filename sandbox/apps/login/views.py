from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User



def home(request):
    return render(request, 'core/home.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('core:home')  # Cambia a la URL de inicio de tu app
        else:
            messages.error(request, 'Credenciales incorrectas')
            return render(request, 'register/login.html')  # Devuelve la vista de login con mensaje de error
    return render(request, 'register/login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            if not User.objects.filter(username=username).exists():
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                messages.success(request, 'Cuenta creada con éxito. Inicia sesión.')
                return redirect('login')
            else:
                messages.error(request, 'El usuario ya existe.')
        else:
            messages.error(request, 'Las contraseñas no coinciden.')
    return render(request, 'registro.html')

def logout_view(request):
    logout(request)
    return redirect('home')
