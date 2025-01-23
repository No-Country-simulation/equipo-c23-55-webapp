from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', include('apps.login.urls', namespace='login')), 
    path('', include('apps.core.urls')),  # Ruta para la página de inicio
    
]
