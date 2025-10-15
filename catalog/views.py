from django.shortcuts import render

from catalog.models import Plant, Category


def index(request):
    plants = Plant.objects.all()
    categories = Category.objects.all()
    context = {
        'title': 'Каталог',
        'categories': categories,
        'plants': plants,
    }
    return render(request, 'catalog/index.html', context=context)


def category_view(request, category_slug):
    categories = Category.objects.all()
    category_slug = categories.get(slug=category_slug)
    plants = Plant.objects.filter(category=category_slug)
    context = {
        'title': 'Каталог',
        'categories': categories,
        'plants': plants,
    }
    return render(request, 'catalog/category.html', context=context)