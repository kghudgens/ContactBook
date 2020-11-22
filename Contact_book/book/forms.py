from django import forms
from .models import ContactBook
from django.forms import ModelForm

class ContactForm(ModelForm):
    
    class Meta:
        model = ContactBook
        fields = ("firstname","lastname","email", "phone_number", "occupation" )
        

form = ContactForm()