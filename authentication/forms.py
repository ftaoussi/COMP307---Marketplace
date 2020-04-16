from django import forms

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
       
       
class SignInForm(forms.Form): 
    username = models.CharField()
    password = models.CharField(widget=forms.PasswordInput)
    
def validate_email (value):
    if not (value.endswith('.com') || value.endswith('.ca') || value.endswith('.net')):
        raise ValidationError ('Invalid E-mail format', code='invalidEmail')
    email = User.objects.filter(email=value)
    if email is not None:
        raise ValidationError('Email not available', code='invalidEmail')

def validate_username (value):
    user = User.objects.filter(username=user)
    if user not None:
        raise ValidationError('Username is taken', code='invalidUsername')
