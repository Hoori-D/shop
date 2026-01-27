from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import ListView

from carts.models import CartItem, Cart
from catalog.models import Plant


class IndexView(ListView):
    model = CartItem
    template_name = 'carts/cart.html'
    context_object_name = 'cart_items'

    def get_queryset(self):
        super().get_queryset()
        cart = Cart.objects.get(user=self.request.user)
        return CartItem.objects.filter(cart=cart)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = f'Корзина {self.request.user}'
        return context


@login_required
def add_item(request, slug):
    item = Plant.objects.get(slug=slug)
    user = request.user
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = cart.orders.all()
    is_in_cart = cart_items.filter(plant=item).exists()
    if is_in_cart:
        cart_item = CartItem.objects.filter(cart=cart, plant=item).first()
        cart_item.quantity += 1
        cart_item.save()
    else:
        CartItem.objects.create(cart=cart ,plant=item)
    if request.session.get('next_page'):
        return redirect(request.session.get('next_page'))
    return redirect(request.META['HTTP_REFERER'])


@login_required
def remove_item(request, slug):
    item = Plant.objects.get(slug=slug)
    user = request.user
    cart = Cart.objects.get(user=request.user)
    CartItem.objects.get(plant=item).delete()
    return redirect(request.META['HTTP_REFERER'])


@login_required
def change_item(request, slug):
    item = Plant.objects.get(slug=slug)
    user = request.user
    cart = Cart.objects.get(user=request.user)
    cart_item = CartItem.objects.filter(cart=cart, plant=item).first()
    cart_quant = cart_item.quantity
    if cart_quant > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect(request.META['HTTP_REFERER'])