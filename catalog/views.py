from django.shortcuts import render

from django.http import Http404

from django.core.paginator import Paginator
from django.views.generic import ListView

from catalog.models import Plant, Category


class IndexView(ListView):
    model = Plant
    template_name = 'catalog/index.html'
    context_object_name = 'plants'
    paginate_by = 3
    ordering = ['name']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Каталог'
        context['active_page'] = self.kwargs.get('page_number')
        return context


class CategoryView(ListView):
    model = Plant
    template_name = 'catalog/category.html'
    context_object_name = 'plants'
    paginate_by = 3
    ordering = ['name']

    def get_queryset(self):
        queryset = super().get_queryset()
        category_slug = self.kwargs.get('category_slug')
        return queryset.filter(category__slug=category_slug)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Категории'
        context['active_page'] = self.kwargs.get('page_number')
        return context


def plant_view(request, plant_slug):
    categories = Category.objects.all()
    plant_by_slug = Plant.objects.get(slug=plant_slug)
    context = {
        'title': 'Каталог',
        'categories': categories,
        'plant_by_slug': plant_by_slug,
    }
    return render(request, 'catalog/plant.html', context=context)