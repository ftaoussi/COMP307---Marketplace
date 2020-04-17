from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	return HttpResponse('Cart view');

def viewCart(request): 
	#
	return HttpResponse("test")

def modifyCart(request, action, product_id):
	#
	return HttpResponse("test")

def checkout(request):
	#
	return HttpResponse("test")

