from django.db import models
<<<<<<< HEAD

# Create your models here.
=======
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    description = models.CharField(null=True, blank=True, max_length=200)
    occupation = models.CharField(null=True, blank=True, max_length=50)
    location = models.CharField(null=True, blank=True, max_length=50)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    linkedin_link = models.CharField(null=True, blank=True, max_length=50)
    github_link = models.CharField(null=True, blank=True, max_length=50)
    youtube_link = models.CharField(null=True, blank=True, max_length=50)
>>>>>>> dev-barahonagallardo
