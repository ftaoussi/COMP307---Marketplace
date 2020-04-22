from product_listing.models import Neighborhood
from django import template

register = template.Library()

@register.inclusion_tag('product_listing/show_neighborhoods.html')
def show_neighborhoods():
    n = Neighborhood.objects.all()
    return {'neighborhoods': n}