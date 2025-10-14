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