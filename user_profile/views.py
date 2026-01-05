from django.shortcuts import render
from django.views.generic import DetailView
from django.contrib.auth import get_user_model


class IndexView(DetailView):
    model = get_user_model()
    template_name = 'user_profile/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Профиль'
        return context