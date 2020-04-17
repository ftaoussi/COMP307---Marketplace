from django import forms
from smart_selects.db_fields import ChainedForeignKey

class ListingForm(forms.Form):
    name = forms.CharField()
    seller = request.user
    price_initial = forms.IntegerField()
    category = forms.ChoiceField(queryset = Category.objects.all())
    #the line below is for the chained/dependent drop down list
    subcategory = forms.ChainedForeignKey(Subcategory, chained_field="category", chained_model_field="category", show_all = False, auto_choose = True, sort=True)
    location = forms.ChoiceField(queryset = Neighborhood.objects.all())
    time = forms.TimeField()
    description = forms.CharField()
    stock = forms.IntegerField()
    size = forms.CharField()
    image = forms.ImageField()
    
