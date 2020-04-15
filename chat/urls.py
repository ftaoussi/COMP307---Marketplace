from django.urls import path

import chat.views

urlpatterns = [
	path('', chat.views.index, name='index'),
]
