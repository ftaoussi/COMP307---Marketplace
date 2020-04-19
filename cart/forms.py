from django import forms

class ShippingForm(forms.Form):
    street_address = forms.TextField()
    postcode = forms.CharField(max_length=7)