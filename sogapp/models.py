from django.db import models

# Create your models here.
# This is the user contact model form for this website.
class UserContactInfo(models.Model):
    first_name = models.CharField(max_length=250, blank=False)
    last_name = models.CharField(max_length=250, blank=False)
    email = models.CharField(max_length=250, blank=False)
    message = models.TextField(blank=False)

    def __str__(self):
        return self.first_name +" "+ self.last_name

class ArtistInfo(models.Model):
    first_name = models.CharField(max_length=150, blank=False)
    last_name = models.CharField(max_length=250, blank=False)
    artist_bio = models.TextField(blank=False)
    artist_photo1_url = models.URLField(blank=False)
    artist_photo2_url = models.URLField(blank=False)
    artist_photo3_url = models.URLField(blank=False)

    def __str__(self):
        return self.first_name + " "+ self.last_name
