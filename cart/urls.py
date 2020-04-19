from django.urls import path

from . import views

app_name = 'cart'
urlpatterns = [
	path('', views.viewCart, name ='viewCart'),
	path('action=<slug:action>&id=<int:product_id>', views.modifyCart, name='modifyCart'),
	path('checkout', views.checkout, name='checkout')
]
