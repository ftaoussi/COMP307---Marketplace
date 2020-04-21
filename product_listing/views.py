from django.shortcuts import render
from django.http import HttpResponse
from product_listing.models import Product, Image
import product_listing.forms

# Create your views here.
def index(request):
    context = {'products': zip(Product.objects.all(), Image.objects.all())}
    return render(request, 'product_listing/index.html', context)

def listItem(request):
    context={}
    if request.method=='POST':
        form = product_listing.forms.ListingForm(request.POST)
        if form.is_valid():
            try:
                product = Product(
                    name = form.cleaned_data['name'],
                    seller = request.user,
                    price_initial = form.cleaned_data['price_initial'],
                    price_current = price_initial,
                    category = form.cleaned_data['category'],
                    subcategory = form.cleaned_data['subcategory'],
                    location = form.cleaned_data['location'],
                    time = form.cleaned_data['time'],
                    description = form.cleaned_data['description'],
                    stock = form.cleaned_data['stock'],
                    size = form.cleaned_data['size']
                )
                product.save()
                image = Image(img=form.cleaned_data['image'], product = product)
                image.save()
                return HttpResponseRedirect(reverse('product_listing/list/'))
            except: 
                form.add_error(None, 'Unable to list product')
        context['form'] = form
    return render(request, 'product_listing/listItem.html', context)

def viewItem(request, product_id): 
    context={}
    product=Product.objects.filter(id=product_id)
    img = Image.objects.filter(product=product)
    context['product'] = product
    context['image'] = img
    return render(request,'product_listing/product.html', context)