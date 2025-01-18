from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import LoginForm


def login_view(request):
    template = 'login/login.html'

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            form_username = form.cleaned_data.get('username')
            form_password = form.cleaned_data.get('password')
            user = authenticate(request, username=form_username, password=form_password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Has accedido a tu cuenta con éxito.')
                return redirect('core:home')
            else:
                messages.error(request, 'Las credenciales de login son incorrectas o no existen.')
    else:
        form = LoginForm()
    context = {'form': form}
    return render(request, template, context)


@login_required(login_url='login:login')
def logout_view(request):
    logout(request)
    return redirect('login:login')
