# apps/login/urls.py

from django.urls import path
from . import views


app_name = 'register'
urlpatterns = [
    path('login/', views.login_view, name='login'),  # Ruta para login
    path('register/', views.register, name='register'),  # Ruta para registro
    path('logout/', views.logout_view, name='logout'),  # Ruta para logout
]
