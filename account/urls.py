from django.urls import path
import account.views

urlpatterns = [
	path('', account.views.index, name='index'),
	path('login', account.views.loginUser, name='login'),
	path('logout', account.views.logout, name='logout'),
	path('signup', account.views.signup, name='signup')
]
