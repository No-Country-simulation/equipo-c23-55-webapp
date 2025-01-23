# sandbox/urls.py

from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', include('apps.login.urls')),  # Incluye las rutas de la app login
    path('', views.home, name='home'),
]
