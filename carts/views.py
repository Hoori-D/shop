from django.views.generic import ListView

from carts.models import CartItem


class IndexView(ListView):
    model = CartItem
    template_name = 'carts/cart.html'
    context_object_name = 'cart_items'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = f'Корзина {self.object_list[0].cart.user.username}'
        return context