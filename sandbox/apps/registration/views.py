from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.views import LoginView

from .forms import RegistrationForm


def registration(request):
    template = 'registration/registration.html'

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Has registrado tu cuenta con éxito.')
            return redirect('core:home')
        else:
            messages.error(request, 'Las credenciales no cumplen con los requisitos o ya existen.')
    else:
        form = RegistrationForm()

    context = {'form': form}
    return render(request, template, context)


class UserLoginView(LoginView):
    def form_invalid(self, form):
        messages.error(self.request, 'Las credenciales de acceso son incorrectas o no existen.')
        return super().form_invalid(form)

    def form_valid(self, form):
        messages.success(self.request, 'Has accedido a tu cuenta con éxito.')
        return super().form_valid(form)
