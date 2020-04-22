from product_listing.models import Subcategory
from django import template

register = template.Library()

@register.inclusion_tag('product_listing/show_subcategories.html')
def show_subcategories():
    s = Subcategory.objects.all()
    return {'subcategories': s}