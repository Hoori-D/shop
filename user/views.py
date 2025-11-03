from django.views.generic import CreateView
from django.contrib.auth.views import LoginView

from user.forms import LoginForm, RegistrationForm


class LoginUserView(LoginView):
    form_class = LoginForm
    template_name = 'user/login.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Вход'
        return context


class RegistrationUserView(CreateView):
    form_class = RegistrationForm
    template_name = 'user/registration.html'
    success_url = 'user:login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Регистрация'
        return context