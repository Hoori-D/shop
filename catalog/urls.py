from django.urls import path
from . import views


app_name='catalog'
urlpatterns = [
    path('search/', views.PlantListView.as_view(), name='search'),
    path('<slug:slug>/', views.PlantListView.as_view(), name='category_by_slug'),
    path('plant/<slug:slug>/', views.PlantDetailView.as_view(), name='plant_by_slug'),
]