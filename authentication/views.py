from django.contrib.auth import authenticate

def signup (request): 
    context={}
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            try:
                user = User.objects.create_user(
                    username=form.cleaned_data['username'],
                    email = form.cleaned_data['email'],
                    password = form.cleaned_data['password']
                )
                return HttpResponseRedirect(reverse('login'))
             except IntegrityError:
                 forms.add_error('username', 'Username is taken')
        context['form'] = form
    return render(request, 'signup', context)
    
    def loginUser(request):
      context={}
      if method=='POST':
        form = forms.SignInForm(request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['name'],password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                forms.add_error('password','Invalid username or password')
        context['form'] = form

    return render(request, 'login', context)
