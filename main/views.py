from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

from catalog.models import Category


@method_decorator(cache_page(60 * 1/6), name='dispatch')
class IndexView(ListView):
    template_name = 'main/index.html'
    model = Category
    context_object_name = 'categories'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Главная страница'
        context['slug'] = 'all'
        return context


@method_decorator(cache_page(60 * 1/6), name='dispatch')
class AboutView(TemplateView):
    template_name = 'main/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'О нас'
        context["content"] = 'О нас'
        context['slug'] = 'all'
        return context
