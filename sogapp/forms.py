from django import forms 
from . models import UserContactInfo

# The user contact form for this website.
class UserContactForm(forms.ModelForm):
    class Meta:
        model = UserContactInfo
        fields = ('first_name', 'last_name', 'email', 'message')