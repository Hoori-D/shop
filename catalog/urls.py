from django.urls import path
from . import views


app_name='catalog'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('category/<slug:slug>/', views.CategoryView.as_view(), name='category_by_slug'),
    path('plant/<slug:slug>/', views.PlantDetailView.as_view(), name='plant_by_slug'),
]