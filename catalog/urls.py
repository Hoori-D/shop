from django.urls import path
from . import views

app_name='catalog'
urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:category_slug>/', views.category_view, name='category_by_slug'),
]