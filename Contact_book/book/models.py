from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class ContactBook(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    email = models.EmailField()

    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)

    occupation = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)
    