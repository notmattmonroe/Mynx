from django.db import models
from aldryn_categories.fields import CategoryManyToManyField
from filer.fields.image import FilerImageField
import datetime

DOW = (('1', 'Sunday'),
      ('2', 'Monday'),
      ('3', 'Tuesday'),
      ('4', 'Wednesday'),
      ('5', 'Thursday'),
      ('6', 'Friday'),
      ('7', 'Saturday'))

class Course(models.Model):
    session_id = models.ForeignKey('Session')
    course_name = models.CharField(blank=False, null=False, max_length=250)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=False, null=False)
    is_workshop = models.BooleanField(default=False)
    all_day = models.BooleanField(default=False)
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    days_of_week = models.CharField(max_length=1, choices=DOW, blank=True)
    custom_start_date = models.DateField(blank=True, null=True)
    custom_end_date = models.DateField(blank=True, null=True)
    is_private = models.BooleanField(default=False)
    spaces = models.IntegerField(default=15)
    instructor = models.ForeignKey('auth.User')
    image =  FilerImageField(null=True, blank=True)
    price = models.IntegerField(blank=True, null=True)
    location = models.ForeignKey('location.Location', null=True)
    category = CategoryManyToManyField()
    dropins = models.BooleanField(default=True)
    dropin_price = models.IntegerField(default=20)
    ticket_link = models.CharField(blank=True, max_length=250)
    create_date = models.DateTimeField(blank=True, null=False, auto_now=True)
    publish_date = models.DateField(blank=False, default=datetime.datetime.now)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.course_name

class Session(models.Model):
    session_name = models.CharField(blank=False, null=False, max_length=250)
    start_date = models.DateField(blank=False, null=False)
    end_date = models.DateField(blank=False, null=False)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.session_name

        