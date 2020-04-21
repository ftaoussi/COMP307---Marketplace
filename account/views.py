from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.db import IntegrityError
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import account.forms
#from product_listing import templates

def signup(request): 
    context = {}
    if request.method == 'POST':
        form = account.forms.SignUpForm(request.POST)
        if form.is_valid():
            try:
                user = User.objects.create_user(
                    username = form.cleaned_data['username'],
                    email = form.cleaned_data['email'],
                    password = form.cleaned_data['password']
                )
                return HttpResponseRedirect(reverse('account:login'))
            except IntegrityError:
                 form.add_error('username', 'Username is taken')
        context['form'] = form
    return render(request, 'account/signup.html', context)
    
def loginUser(request):
    context={}
    if request.method=='POST':
        form = account.forms.SignInForm(request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['username'],password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('product_listing/index.html'))
            else:
                form.add_error(None,'Invalid username or password')
        else:
            form.add_error(None,'Invalid input')
        context['form'] = form
    return render(request, 'account/login.html', context)

def index(request):
    if request.user.is_authenticated:
        context={}
        #assign context variables
        return render(request, 'account/index.html', context)
    return redirect('/account/login.html') 

@login_required
def do_logout(request):
    logout(request)
    return render(request, 'product_listing/index.html')
