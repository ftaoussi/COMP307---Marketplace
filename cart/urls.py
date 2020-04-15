from django.urls import path

import cart.views

urlpatterns = [
	path('', cart.views.index, name='index'),
]
