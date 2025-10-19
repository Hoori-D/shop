from django.shortcuts import render

# Create your views here.


def login(request):
    context = {
        'title': 'Вход'
    }
    return render(request, 'user/login.html', context)