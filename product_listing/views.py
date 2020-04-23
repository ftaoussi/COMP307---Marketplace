from django.shortcuts import render
from django.http import HttpResponse
from product_listing.models import Product, Image
import product_listing.forms
import datetime

# Create your views here.
def index(request):
    context = {'products': zip(Product.objects.all(), Image.objects.all())}
    return render(request, 'product_listing/index.html', context)

def delete_listing(request):
    return render(request, 'product_listing/delete_listing.html', {})

def listItem(request):
    context={'products': Product.objects.all()} #added context so that it can be used in listing the history automatically
    if request.method=='POST':
        print('post')
        form = product_listing.forms.ListingForm(request.POST, request.FILES)
        if form.is_valid():
            print('valid')
            try:
                print('ok')
                product = Product(
                    name = form.cleaned_data['name'],
                    seller = request.user,
                    price_initial= form.cleaned_data['price'],
                    price_current = form.cleaned_data['price'],
                    category = form.cleaned_data['category'],
                    subcategory = form.cleaned_data['subcategory'],
                    location = form.cleaned_data['location'],
                    time = datetime.datetime.now(),
                    description = form.cleaned_data['description'],
                    stock = form.cleaned_data['stock'],
                    size = form.cleaned_data['size']
                )
                product.save()
                print('product ok')
                image = Image(img=form.cleaned_data['image'], product=product)
                image.save()
                print('image ok')
                return render(request, 'product_listing/index.html', context)
            except: 
                print('error1')
                form.add_error(None, 'Unable to list product')
                
        print('invalid')
    context['form'] = product_listing.forms.ListingForm
    return render(request, 'product_listing/listItem.html', context)

def viewItem(request, product_id): 
    context={}
    product=Product.objects.get(id=product_id)
    img = Image.objects.get(product=product)
    context = {'product': product, 'image': img, 'pid': product_id}
    return render(request,'product_listing/product.html', context)
