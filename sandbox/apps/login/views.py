from django.contrib.auth import  login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect

from django.contrib.auth.forms import AuthenticationForm 



from django.contrib.auth.forms import UserCreationForm


def registro_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Te has registrado con éxito. Ya puedes iniciar sesión.')
            return redirect('login:login')  # Redirige a la página de login después del registro.
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'registro.html', context)





def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Bienvenido de nuevo!")
            return redirect('home')  # Redirige a una página de inicio después del login
        else:
            messages.error(request, "Nombre de usuario o contraseña incorrectos.")
    else:
        form = AuthenticationForm()

    
        return render(request, 'login/login.html', {'form': form})



@login_required(login_url='login:login')
def logout_view(request):
    logout(request)
    return redirect('login:login')
