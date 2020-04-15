from django.generic import ListView
from smart_selects.db_fields import ChainedForeignKey
from django.contrib.auth import authenticate

#these two classes are just incase we need to be able to list the categories or neighborhoods on one of the webpages
class NeighborhoodListView (ListView):
    model = Neighborhood
    context-object-name['neighborhood']

class CategoryListView (ListView): 
    model = Category
    context-object-name['category']

#signup form
class SignupForm(forms.Form): 
    username = forms.CharField()
    email = models.EmailField(
        validators=[validate_email]
        error_messages={'invalid': 'Invalid E-Mail Address'}
    )
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super(SignUpForm, self).clean()
        if 'password' in cleaned_data and 'confirm_password' in cleaned_data and cleaned_data['password'] != cleaned_data['confirm_password']:
            self.add_error('confirm_password', 'Passwords do not match')
        return cleaned_data
#listing form
class ListingForm(forms.Form):
    name = models.CharField()
    seller = request.user
    price_initial = models.IntegerField()
    category = model.ChoiceField(queryset = Category.objects.all())
    #the line below is for the chained/dependent drop down list
    subcategory = model.ChainedForeignKey(Subcategory, chained_field="category", chained_model_field="category", show_all = False, auto_choose = True, sort=True)
    location = model.ChoiceField(queryset = Neighborhood.objects.all())
    time = models.TimeField()
    description = models.CharField()
    stock = models.IntegerField()
    size = model.CharField()
    image = model.ImageField()


#validator for e-mail, default django e-mail validator accepts non-email values such as example@domain.12
def validate_email (value):
    if not (value.endswith('.com') || value.endswith('.ca') || value.endswith('.net')):
        raise ValidationError ('Invalid E-mail format', code='invalid')
#function-based view for domain.com/list, if the request is a GET request it renders the 'list' page, if the request is POST it instantiates a listing
def listItem(request):
    context={}
    if request.method=='POST':
        form = forms.ListingForm(request.POST)
        if form.is_valid():
            try:
                listing = Listing(
                    name = form.cleaned_data['name'],
                    seller = form.cleaned_data['seller'],
                    price_initial = form.cleaned_data['price_initial'],
                    price_current = price_initial
                    category = form.cleaned_data['category'],
                    subcategory = form.cleaned_data['subcategory'],
                    location = form.cleaned_data['location'],
                    time = form.cleaned_data['time'],
                    description = form.cleaned_data['description'],
                    stock = form.cleaned_data['stock'],
                    size = form.cleaned_data['size']
                )
                listing.save()
                image = Image(form.cleaned_data['image'])
                image.save()
                return HttpResponseRedirect(reverse('index'))
            except: 
                forms.add_error('server', 'Server Error')
        context['form'] = form
        return render(request, 'list', context)


#same idea but for sign-up
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

