from django import template
from django.utils.http import urlencode

from carts.models import Cart, CartItem
from catalog.models import Category


register = template.Library()


@register.inclusion_tag('catalog/list_categories.html')
def tag_categories():
    categories = Category.objects.all()
    return {'categories': categories}


@register.simple_tag(takes_context=True)
def tag_quantity(context, plant):
    user = context.get('request').user
    cart = Cart.objects.get(user=user)
    item = CartItem.objects.filter(plant=plant, cart=cart)
    if item.exists():
        return item.first().quantity
    else:
        return None


@register.simple_tag(takes_context=True)
def change_params(context, **kwargs):
    query = context['request'].GET.dict()
    query.update(kwargs)
    return urlencode(query)
