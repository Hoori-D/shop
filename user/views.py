from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView

from user.forms import LoginForm, RegistrationForm


class LoginUserView(LoginView):
    form_class = LoginForm
    template_name = 'user/login.html'

    def get(self, request, *args, **kwargs):
        plant_slug = self.request.GET.get('plant_slug')
        if plant_slug:
            request.session['adding_plant_slug'] = plant_slug
            request.session['prev_page'] = request.META['HTTP_REFERER']
        return super().get(request, *args, **kwargs)

    def get_success_url(self):
        prev_page = super().get_success_url()
        plant_slug = self.request.session.get('adding_plant_slug')
        if plant_slug:
            del self.request.session['adding_plant_slug']
            return reverse('carts:add_item', kwargs={'slug': plant_slug})
        return prev_page

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Вход'
        return context


class RegistrationUserView(CreateView):
    form_class = RegistrationForm
    template_name = 'user/registration.html'
    success_url = reverse_lazy('user:login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Регистрация'
        return context