from product_listing.models import Product
from django import template

register = template.Library()

@register.inclusion_tag('product_listing/show_products.html')
def show_products():
    p = Product.objects.all()
    return {'products': p}