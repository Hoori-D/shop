from django.shortcuts import render

from django.http import Http404

from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView

from catalog.models import Plant, Category


class IndexView(ListView):
    model = Plant
    template_name = 'catalog/index.html'
    context_object_name = 'plants'
    paginate_by = 3
    ordering = ['name']

    def get_queryset(self):
        qs = super().get_queryset()
        order = self.request.GET.get('order')
        if not order or order == 'default' :
            return qs
        return qs.order_by(order)

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
        category_slug = self.kwargs.get('slug')
        return queryset.filter(category__slug=category_slug)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.object_list:
            context["title"] = self.object_list[0].category.name
        else:
            context["title"] = 'Товары не найдены'
        context['active_page'] = self.kwargs.get('page_number')
        return context


class PlantDetailView(DetailView):
    model = Plant
    template_name = 'catalog/plant.html'
    context_object_name = 'plant_by_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.object.name
        return context