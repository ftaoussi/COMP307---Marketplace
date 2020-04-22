from django import forms

class ShippingForm(forms.Form):
    street_address = forms.CharField(max_length=40)
    postcode = forms.CharField(max_length=7)