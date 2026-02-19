from django.db.models import F, Q
from django.db.models import Sum, Count
from django.shortcuts import render, get_object_or_404

from django.http import Http404

from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView

from carts.models import Cart
from catalog.models import Plant, Category
from catalog.utils import q_search


class PlantListView(ListView):
    model = Plant
    template_name = 'catalog/index.html'
    context_object_name = 'plants'
    paginate_by = 3
    ordering = ['-views_count']

    def get_template_names(self):
        if self.request.headers.get('HX-Request'):
            return ['catalog/partials/plants_list.html']
        return [self.template_name]

    def get_queryset(self):
        qs = super().get_queryset()
        order = self.request.GET.get('order')
        category_slug = self.kwargs.get('slug', 'all')
        query = self.request.GET.get('q')

        if query:
            category_slug = None
            qs = q_search(query)

        if self.kwargs.get('slug') != 'all' and not self.kwargs.get('slug') is None:
            qs =  qs.filter(category__slug=category_slug)

        if not order or order == 'default' :
            if self.request.user.is_authenticated:
                cart = Cart.objects.filter(user=self.request.user).first()
                return qs.annotate(total_in_cart=Sum('orders__quantity', filter=Q(orders__cart=cart)))
            else:
                return qs
        if self.request.user.is_authenticated:
            cart = Cart.objects.filter(user=self.request.user).first()
            return qs.order_by(order).annotate(total_in_cart=Sum('orders__quantity', filter=Q(orders__cart=cart)))
        else:
            return qs.order_by(order)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['slug'] = self.kwargs.get('slug', 'all')
        context['active_page'] = self.request.GET.get('page')
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

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        self.model.objects.filter(pk=obj.pk).update(views_count=F('views_count') + 1)
        obj.refresh_from_db()
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.object.name
        return context