from django import template

from catalog.models import Category


register = template.Library()


@register.inclusion_tag('catalog/list_categories.html')
def tag_categories():
    categories = Category.objects.all()
    return {'categories': categories}