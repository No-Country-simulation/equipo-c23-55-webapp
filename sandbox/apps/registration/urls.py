from django.urls import path, include

from . import views

app_name = 'registration'
urlpatterns = [
    path('registration/', views.registration, name='registration'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('', include('django.contrib.auth.urls')),
]
