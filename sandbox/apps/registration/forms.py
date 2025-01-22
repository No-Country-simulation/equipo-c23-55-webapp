from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from apps.users.models import CustomUser


class RegistrationForm(UserCreationForm):
    username = forms.CharField(required=True, max_length=50)
    group = forms.ModelChoiceField(queryset=Group.objects.all(), required=True)
    email = forms.EmailField(required=True, max_length=50)

    class Meta:
        model = CustomUser
        fields = ('username', 'group', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user_group = self.cleaned_data['group']
        if commit:
            user.save()
            user.groups.add(user_group)
        return user


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=50)
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput())

    class Meta:
        model = CustomUser
        fields = ['username', 'password']
