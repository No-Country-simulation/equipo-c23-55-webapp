from django.contrib.auth.views import LoginView
from django.contrib import messages


class UserLoginView(LoginView):
    def form_invalid(self, form):
        messages.error(self.request, 'Las credenciales de acceso son incorrectas o no existen.')
        return super().form_invalid(form)

    def form_valid(self, form):
        messages.success(self.request, 'Has accedido a tu cuenta con éxito.')
        return super().form_valid(form)
