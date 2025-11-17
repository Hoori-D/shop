from django.urls import path
from . import views


app_name='catalog'
urlpatterns = [
    path('<slug:slug>/', views.IndexView.as_view(), name='category_by_slug'),
    path('plant/<slug:slug>/', views.PlantDetailView.as_view(), name='plant_by_slug'),
]