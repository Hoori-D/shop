from django.urls import path
from . import views


app_name='user'
urlpatterns = [
    path('login/', views.LoginUserView.as_view(), name='login'),
    path('registration/', views.RegistrationView.as_view(), name='registration'),
]