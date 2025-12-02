from django.contrib import admin

from carts.models import Cart, CartItem


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 'created_at']

    search_fields = ['user']

    ordering = ['user']
    sortable_by = ['name']


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['cart', 'plant', 'quantity', 'created_at']

    search_fields = ['cart']

    ordering = ['cart']
    sortable_by = ['cart']