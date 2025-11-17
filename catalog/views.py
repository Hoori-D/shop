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
        category_slug = self.kwargs.get('slug', 'all')
        if self.kwargs.get('slug') != 'all':
            qs =  qs.filter(category__slug=category_slug)
        if not order or order == 'default' :
            return qs
        return qs.order_by(order)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['slug'] = self.kwargs.get('slug', 'all')
        context['active_page'] = self.kwargs.get('page_number')
        if self.kwargs.get('slug') != 'all':
            if self.object_list:
                context["title"] = f'Каталог:{self.object_list[0].category.name}'
            else:
                context["title"] = 'Товары не найдены'
        else:
            context["title"] = 'Каталог'
        return context


class PlantDetailView(DetailView):
    model = Plant
    template_name = 'catalog/plant.html'
    context_object_name = 'plant_by_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.object.name
        return context