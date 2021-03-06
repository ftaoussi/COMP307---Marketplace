from django.urls import path
from django.conf.urls.static import static
from product_listing import views

app_name = 'product_listing'
urlpatterns = [
	path('', views.index, name='index'),
	path('<int:id>/delete_listing/', views.want_delete_listing, name ='delete_listing'),
    path('<int:id>/delete_listing/delete_success/', views.delete_listing, name ='delete_listing'),
	path('<int:id>/modify_listing/', views.modify_listing, name ='modify_listing'),
	path('list/', views.listItem, name ='listItem'),
	path('<int:product_id>', views.viewItem)
]
