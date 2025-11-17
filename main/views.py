from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

from catalog.models import Category


class IndexView(ListView):
    template_name = 'main/index.html'
    model = Category
    context_object_name = 'categories'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Главная страница'
        context['slug'] = 'all'
        return context


class AboutView(TemplateView):
    template_name = 'main/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'О нас'
        context["content"] = 'О нас'
        context['slug'] = 'all'
        return context
