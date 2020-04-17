from django.urls import path

from product_listing import views

urlpatterns = [
	path('', views.index, name='index'),
	path('list/', views.listItem, name ='listItem'),
	path('<int:product_id>', views.viewItem)
]
