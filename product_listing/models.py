from django.db import models 
from django.contrib.auth.models import User 


class Category(models.Model): 
    name = models.CharField(unique=True)
    def __str__ (self):
        return self.name
class Subcategory(models.Model): 
    name = models.CharField(unique=True)
    parent_category = models.ForeignKey(Category, on.delete=models.CASCADE)
    def __str__(self):
        return self.name

class Neighborhood(models.Model): 
    name = models.CharField(unique=true)
    def __str__(self):
        str1 = self.name
        return str1

class Listings(models.Model):
    name = models.CharField(max_length=30)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    price_current = models.IntegerField()
    price_initial = models.IntegerField(blank=False)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.SET_NULL)
    location = model.ForeignKey(Neighborhood, on_delete=models.SET_NULL)
    time = models.CharField(max_length=16)
    description = models.CharField()
    stock = models.IntegerField()
    size = models.CharField()
    option = models.CharField()
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("", kwargs={id = self.id})

class Orders(models.Model):
    seller = models.ForeignKey(User)
    buyer = models.ForeignKey(User)
    product = models.ForeignKey(Product)
    time = models.CharField()
    price = models.IntegerField()
    shipping_from = models.CharField()
    shipping_to = models.CharField()
    #PAYMENT_CHOICES=['PAYPAL','CASH']
    #method_of_payment = models.CharField(choices=PAYMENT_CHOICES)

    def __str__(self):
        str1=seller.__str__()
        str2=product.__str__()
        str3=buyer.__str__()
        return (str1+" -> "+str2+" ->"str3)
    
class Image(models.Model): 
    img = models.ImageField
    listing = models.ForeignKey(Listings, on_delete=models.CASCADE)
