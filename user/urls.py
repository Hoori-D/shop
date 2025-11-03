from django.urls import path
from django.contrib.auth.views import LogoutView

from . import views


app_name='user'
urlpatterns = [
    path('login/', views.LoginUserView.as_view(), name='login'),
    path('registration/', views.RegistrationUserView.as_view(), name='registration'),
    path('logout/', LogoutView.as_view(), name='logout'),
]