from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	return HttpResponse('Currently on the main page of the site: will display a list of all the items for sale.');
