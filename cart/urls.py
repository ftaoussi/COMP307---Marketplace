from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name ='index'),
	path('action=<slug:action>&id=<int:product_id>&option=<slug:option>', views.modifyCart, name='modifyCart'),
	path('checkout', views.checkout, name='checkout')
]
