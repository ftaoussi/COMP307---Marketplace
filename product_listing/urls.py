from django.urls import path

import product_listing.views

urlpatterns = [
	path('', product_listing.views.index, name='index'),
]
