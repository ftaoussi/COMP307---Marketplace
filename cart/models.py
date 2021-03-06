from django.db import models
from product_listing.models import Product
from account.models import User

# Create your models here.

#Items belong to a cart
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    
    def __str__(self):
        return self.user.__str__()

class Item(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    unit_price = models.IntegerField()
    
    def __str__(self):
        return self.product.__str__() + ", " + self.cart.__str__()

class Basket(models.Model):
    seller = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='basket_buyer')
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='basket_seller')
    time = models.TextField()
    shipping_to=models.TextField()

    def __str__(self):
        str1 = self.seller.__str__()
        str2 = self.buyer.__str__()
        return str1+str2
#orderitems are created after an order is confirmed, and belong to a basket
class OrderItem(models.Model):
    product_string = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orderitem_buyer')
    seller = models.ForeignKey(User, on_delete =models.DO_NOTHING, related_name='orderitem_seller')
    unit_price = models.IntegerField()
    quantity = models.IntegerField()
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE, null=True)
    shipping_to = models.TextField()

    def __str__(self):
        str1 = self.seller.__str__()
        str2 = self.buyer.__str__()
        str3 = self.product.__str__()
        return str1+str2+str3






