from django import forms
from product_listing.models import Category, Neighborhood, Subcategory

class ListingForm(forms.Form):
    name = forms.CharField()
    price = forms.IntegerField()
    category = forms.ModelChoiceField(queryset = Category.objects.all())
    subcategory = forms.ModelChoiceField(queryset=Subcategory.objects.all())
    location = forms.ModelChoiceField(queryset = Neighborhood.objects.all())
    description = forms.CharField()
    stock = forms.IntegerField()
    size = forms.CharField()
    image = forms.ImageField()