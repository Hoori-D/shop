from django.shortcuts import render

from catalog.models import Category


def index(request):
    categories = Category.objects.all()

    context = {
        'title': 'Главная страница',
        'categories': categories,
    }

    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'О нас',
        'content': 'О нас',
    }

    return render(request, 'main/about.html', context)
