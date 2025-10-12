from django.shortcuts import render

from catalog.models import Plant


def index(request):
    plants = Plant.objects.all()
    context = {
        'title': 'Каталог',
        'plants': plants,
    }
    return render(request, 'catalog/index.html', context=context)