from django.urls import path
from . import views

app_name='user_profile'
urlpatterns = [
    path('<int:pk>/', views.ProfileChange.as_view(), name='index'),
]