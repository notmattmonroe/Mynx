from django.db import models

# Create your models here.

class Location(models.Model):
    location_name = models.CharField(blank=False, null=False, max_length=250)
    location_slug = models.CharField(max_length=100, blank=False, null=False)
    location_address = models.CharField(max_length=200, blank=False, null=False)
    location_address2 = models.CharField(max_length=200, blank=True, null=True)
    location_city = models.CharField(max_length=200, blank=False, null=False)
    location_state = models.CharField(max_length=2, blank=False, null=False)
    location_postcode = models.CharField(max_length=10, blank=True, null=True)
    location_phone = models.CharField(max_length=15, blank=True, null=True)
    location_website = models.CharField(max_length=255, blank=True, null=True)
    #google maps linkage
    #location_country = models.CharField(max_length=2, blank=True, null=True)

    def __str__(self):
        return self.location_name
