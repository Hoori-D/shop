from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        'title': 'Каталог',
        'content': 'Товары',
    }
    return render(request, 'catalog/index.html', context=context)