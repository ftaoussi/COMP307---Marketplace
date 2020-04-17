from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	return HttpResponse('Cart view');

def viewCart(request): 
	#

def modifyCart(request, action, product_id):
	#

def checkout(request):
	#

