from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.contrib.auth.views import LoginView

from user.forms import LoginForm


class LoginUserView(LoginView):
    form_class = AuthenticationForm
    template_name = 'user/login.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Вход'
        return context


class RegistrationView(TemplateView):
    template_name = 'user/registration.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Регистрация'
        return context