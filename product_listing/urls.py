from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('list/', views.listItem, name ='listItem')
	path('<int:product_id>/', views.viewItem)
]
