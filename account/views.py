from django.contrib.auth import authenticate
from django.shortcuts import render
from django.http import HttpResponse
import account.forms

def signup (request): 
    context={}
    if request.method == 'POST':
        form = account.forms.SignupForm(request.POST)
        if form.is_valid():
            try:
                user = User.obje
                cts.create_user(
                    username=form.cleaned_data['username'],
                    email = form.cleaned_data['email'],
                    password = form.cleaned_data['password']
                )
                return HttpResponseRedirect(reverse('login'))
            except IntegrityError:
                 forms.add_error('username', 'Username is taken')
        context['form'] = form
    return render(request, 'account/signup.html', context)
    
def loginUser(request):
    context={}
    if method=='POST':
        form = account.forms.SignInForm(request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['name'],password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('index.html'))
            else:
                forms.add_error('password','Invalid username or password')
        context['form'] = form
    return render(request, 'account/login.html', context)

def index(request): 
    context={}
    return render(request, 'account/index.html', context)

def logout(request):
    return HttpResponse("Logged out.")
    #implementation
