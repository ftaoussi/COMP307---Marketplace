from django.urls import path

from product_listing import views

app_name = 'product_listing'
urlpatterns = [
	path('', views.index, name='index'),
	path('list/', views.listItem, name ='listItem'),
	path('<int:product_id>', views.viewItem)
]
