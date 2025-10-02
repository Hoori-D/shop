from django.shortcuts import render


def index(request):
    context = {
        'title': 'Главная страница',
        'content': 'Главная',
    }

    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'О нас',
        'content': 'О нас',
    }

    return render(request, 'main/about.html', context)
