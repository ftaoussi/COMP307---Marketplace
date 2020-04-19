from django.urls import path
from django.conf.urls import url

import account.views

app_name = 'account'
urlpatterns = [
	path('', account.views.index, name='index'),
	path('login/', account.views.loginUser, name='login'),
	url(r'^logout/$', account.views.do_logout, name='logout'),
	path('signup/', account.views.signup, name='signup')
]