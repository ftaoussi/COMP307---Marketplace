from django.db import models 
from account.models import User 



class Category(models.Model): 
    name = models.TextField(unique=True)
    def __str__ (self):
        return self.name
class Subcategory(models.Model): 
    name = models.TextField(unique=True)
    parent_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Neighborhood(models.Model): 
    name = models.TextField(unique=True)
    def __str__(self):
        str1 = self.name
        return str1

class Product(models.Model):
    name = models.CharField(max_length=30)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    price_current = models.IntegerField()
    price_initial = models.IntegerField(blank=False)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.SET_NULL, null=True)
    location = models.ForeignKey(Neighborhood, on_delete=models.SET_NULL, null=True)
    time = models.TextField()
    description = models.TextField()
    stock = models.IntegerField()
    size = models.CharField(max_length=10)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return "/product/%i/" % self.id

class Orders(models.Model):
    seller = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="seller")
    buyer = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="buyer")
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    time = models.TextField()
    price = models.IntegerField()
    shipping_from = models.TextField()
    shipping_to = models.TextField()
    #PAYMENT_CHOICES=['PAYPAL','CASH']
    #method_of_payment = models.CharField(choices=PAYMENT_CHOICES)

    def __str__(self):
        str1=seller.__str__()
        str2=product.__str__()
        str3=buyer.__str__()
        return (str1 + ", " + str2 + ", " + str3)
    
class Image(models.Model): 
    img = models.ImageField
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
