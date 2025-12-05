from django.urls import path
from . import views

app_name='carts'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('add_item/<slug:slug>', views.add_item, name='add_item'),
    path('change_item/<slug:slug>', views.change_item, name='change_item'),
    path('remove_item/<slug:slug>', views.remove_item, name='remove_item'),
]
