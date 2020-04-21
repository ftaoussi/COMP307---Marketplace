from django.contrib import admin

from product_listing.models import Product, Category, Neighborhood

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Neighborhood)