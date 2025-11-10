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


def category_view(request, category_slug, page_number=1):
    category_by_slug = Category.objects.get(slug=category_slug)
    plants = Plant.objects.filter(category=category_by_slug)
    pages = Paginator(plants, 3)

    if page_number in pages.page_range:
        cur_page_plants = pages.page(page_number).object_list
        has_next_page = pages.page(page_number).has_next()
        if has_next_page:
            next_page_number = pages.page(page_number).next_page_number()
        else:
            next_page_number = None
        has_prev_page = pages.page(page_number).has_previous()
        if has_prev_page:
            prev_page_number = pages.page(page_number).previous_page_number()
        else:
            prev_page_number = None
    else:
        raise Http404('Out of range pages')
    context = {
        'title': 'Каталог',
        'category': category_by_slug,
        'plants': cur_page_plants,
        'pages': pages,
        'active_page': page_number,
        'has_next_page': has_next_page,
        'has_prev_page': has_prev_page,
        'next_page_number': next_page_number,
        'prev_page_number': prev_page_number,
    }
    return render(request, 'catalog/category.html', context=context)


def plant_view(request, plant_slug):
    categories = Category.objects.all()
    plant_by_slug = Plant.objects.get(slug=plant_slug)
    context = {
        'title': 'Каталог',
        'categories': categories,
        'plant_by_slug': plant_by_slug,
    }
    return render(request, 'catalog/plant.html', context=context)