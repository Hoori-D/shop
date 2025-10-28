from django.shortcuts import render

from django.views.generic.base import TemplateView

from catalog.models import Category


def index(request):
    categories = Category.objects.all()

    context = {
        'title': 'Главная страница',
        'categories': categories,
    }

    return render(request, 'main/index.html', context)

class AboutView(TemplateView):
    template_name = 'main/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'О нас'
        context["content"] = 'О нас'
        return context
