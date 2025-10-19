from django.urls import path
from . import views


app_name='user'
urlpatterns = [
    path('user', views.login, name='login'),
    path('registration', views.registration, name='registration'),
]