from django.contrib import admin

from product_listing.models import Product, Category, Neighborhood, Subcategory, Image

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Neighborhood)
admin.site.register(Subcategory)
admin.site.register(Image)