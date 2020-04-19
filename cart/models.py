from django.db import models
from product_listing.models import Product
from account.models import User

# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE, relate_name='user')

class Item(models.Model):
    product = models.ForeignKey(Product, on_delete=CASCADE)
    cart = models.ForeignKey(Cart, on_delete=CASCADE)
    quantity = models.IntegerField()
    unit_price = models.IntegerField()

class OrderItem(models.Model):
    product_string = models.TextField()
    product = models.ForeignKey(Product, on_delete=DO_NOTHING)
    buyer = models.ForeignKey(User, on_delete=CASCADE)
    seller = models.ForeignKey(User, on_delete =DO_NOTHING)
    unit_price = models.IntegerField()
    quantity
    basket = models.ForeignKey(Basket, on_delete=CASCADE, null=True)
    shipping_to = models.TextField9)

class Basket(models.Model):
    seller = models.ForeignKey(User, on_delete=DO_NOTHING)
    buyer = models.ForeignKey(User, on_delete=CASCADE)
    time = models.TextField()
    shipping_to=models.TextField()




