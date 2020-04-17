from django.forms import ModelForm
from django.db import models
from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

class SignupForm(forms.Form): 
    username = forms.CharField()
    email = forms.EmailField(
        validators=[validate_email]
    )
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super(SignUpForm, self).clean()
        if 'password' in cleaned_data and 'confirm_password' in cleaned_data and cleaned_data['password'] != cleaned_data['confirm_password']:
            self.add_error('confirm_password', 'Passwords do not match')
        return cleaned_data
       
       
class SignInForm(forms.Form): 
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    
def validate_email (value):
    valid = (value.endswith('.com') or value.endswith('.ca') or value.endswith('.net'))
    if not valid:
        raise ValidationError ('Invalid E-mail format', code='invalidEmail')
    email = User.objects.filter(email=value)
    if email is not None:
        raise ValidationError('Email not available', code='invalidEmail')

def validate_username (value):
    user = User.objects.filter(username=user)
    if user is not None:
        raise ValidationError('Username is taken', code='invalidUsername')
