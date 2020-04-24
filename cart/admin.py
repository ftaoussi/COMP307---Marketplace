from django.contrib import admin
from cart.models import Cart, Item, OrderItem, Basket

# Register your models here.

admin.site.register(Cart)
admin.site.register(Item)
admin.site.register(OrderItem)
admin.site.register(Basket)