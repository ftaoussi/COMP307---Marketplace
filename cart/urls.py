from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('cart', views.viewCart, name ='viewCart')
	path('cart?action=<string: action>&id=<int: product_id>', views.modifyCart, name='modifyCart')
	path('checkout', views.checkout, name='checkout')
]
