from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required(login_url='registration:login')
def home(request):
    template = 'core/home.html'
    return render(request, template)
