# Signal thats fired when something is saved
from django.db.models.signals import post_save
# Whats being saved
from django.contrib.auth.models import User
# receives the the user signal that is being posted 
from django.dispatch import receiver
# Import the profile model that needs to be saved and linked ot the User
from .models import Profile

# When a user is saved send this signal, it will be received by the create Profile
# function, an instance == User, if created the make a profile with the instance
# of the User
@receiver(post_save, sender=User) 
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# Takes the instance created and saves it to the database
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()