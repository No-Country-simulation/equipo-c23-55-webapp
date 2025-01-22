from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'first_name', 'last_name', 'email', 'last_login', 'date_joined', 'occupation', 'location')
    search_fields = ('username', 'first_name', 'last_name', 'email', 'last_login', 'date_joined', 'occupation', 'location')
    
    # Corregir los fieldsets para evitar duplicación
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal information', {'fields': ('first_name', 'last_name', 'email', 'occupation', 'location', 'description', 'profile_picture', 'linkedin_link', 'github_link', 'youtube_link')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    
    list_filter = ('is_active', 'is_staff', 'is_superuser', 'groups')


admin.site.register(CustomUser, CustomUserAdmin)
