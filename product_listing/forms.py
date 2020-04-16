from django import forms
from smart_selects.db_fields import ChainedForeignKey

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
    
