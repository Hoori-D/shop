from django.urls import path
from . import views


app_name='catalog'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('category/<slug:category_slug>/page=<int:page_number>/', views.category_view, name='category_by_slug'),
    path('plant/<slug:plant_slug>/', views.plant_view, name='plant_by_slug'),
]