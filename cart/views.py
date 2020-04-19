from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	context = {}
	return render(request, 'cart/cart.html', context)

def modifyCart(request, action, product_id):
	#
	return HttpResponse("test")

def checkout(request):
	#
	return HttpResponse("test")

