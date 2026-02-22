from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.cache import cache_page
from django.views.generic import DetailView
from django.contrib.auth import get_user_model

from user_profile.forms import ProfileForm, UserForm
from user_profile.models import Profile


class IndexView(UserPassesTestMixin, LoginRequiredMixin, DetailView):
    model = get_user_model()
    template_name = 'user_profile/index.html'

    def test_func(self):
        return self.request.user.id == self.get_object().id

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Профиль'
        return context


@method_decorator(cache_page(600, key_prefix='profile_page'), name='dispatch')
class ProfileChange(UserPassesTestMixin, LoginRequiredMixin, View):
    template_name = 'user_profile/index.html'

    def test_func(self):
        user_id = self.kwargs.get('pk')
        return self.request.user.id == user_id

    def get(self, request, *args, **kwargs):
        user_obj = request.user
        mail = user_obj.email
        profile, created = Profile.objects.get_or_create(user=user_obj)
        profile_form = ProfileForm(instance=profile)
        user_form = UserForm(instance=user_obj)
        return render(request,
                      'user_profile/index.html',
                      {
                          'profile_form': profile_form, 'user_form': user_form,
                          'title': f'Профиль - {user_obj.username}'
                      })

    def post(self, request, *args, **kwargs):
        user_obj = request.user
        mail = user_obj.email
        profile, created = Profile.objects.get_or_create(user=user_obj)
        profile_form = ProfileForm(request.POST,
                                   request.FILES,
                                   instance=profile)
        user_form = UserForm(request.POST,
                             instance=user_obj)
        if profile_form.is_valid():
            if profile_form.has_changed():
                messages.success(request,
                                 "Профиль обновлен")
            profile_form.save()
        if user_form.is_valid():
            if user_form.has_changed():
                changed_fields = user_form.changed_data
                if 'email' in changed_fields:
                    send_mail("Subject here",
                              "Here is the message.",
                              "from@example.com",
                              [mail],
                              fail_silently=False, )
                    messages.success(request,
                                     "Почта обновлена")
                messages.success(request,
                                 "Пользователь обновлен")
            user_form.save()

        return redirect(reverse('user_profile:index', kwargs={'pk': user_obj.id}))