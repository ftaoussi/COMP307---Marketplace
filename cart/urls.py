from django.urls import path

from . import views

app_name = 'cart'
urlpatterns = [
	path('', views.index, name ='index'),
	path('action=<slug:action>&id=<int:product_id>&quantity=<int:quantity>', views.modifyCart, name='modifyCart'),
	path('checkout/', views.checkout, name='checkout'),
	path('checkoutsuccess/', views.checkoutsuccess, name='checkoutsuccess'),
	path('remove_from_cart/', views.remove_from_cart, name='remove-from-cart')
]
