from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	return HttpResponse('Currently on the main page of the site: will display a list of all the items for sale.');
def listItem(request):
    context={}
    if request.method=='POST':
        form = forms.ListingForm(request.POST)
        if form.is_valid():
            try:
                itemListing = Listing(
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
                itemListing.save()
                image = Image(img=form.cleaned_data['image'],listing = itemListing)
                image.save()
                return HttpResponseRedirect(reverse('index'))
            except: 
                forms.add_error(None, 'Unable to make listing')
        context['form'] = form
    return render(request, 'list', context)
