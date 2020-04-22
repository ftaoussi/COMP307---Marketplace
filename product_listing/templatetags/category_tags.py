from product_listing.models import Category
from django import template

register = template.Library()

@register.inclusion_tag('product_listing/show_categories.html')
def show_categories():
    c = Category.objects.all()
    return {'categories': c}