from django.db import models
from django.conf import settings
from filer.fields.image import FilerImageField
import recurrence.fields

class show(models.Model):
    show_name       = models.CharField(max_length=120)
    show_date       = models.DateField()
    show_end_date   = models.DateField(null=True)
    venue_id        = models.ForeignKey('location.Location', null=True)
    show_start      = models.TimeField()
    show_end_time   = models.TimeField()
    show_doors      = models.TimeField(null=True)
    show_recurring  = recurrence.fields.RecurrenceField(null=True)
    show_image = FilerImageField(null=True, blank=True)
    show_notes           = models.TextField(db_column='Notes', blank=True)
    show_ticket_link = models.CharField(blank=True, null=True, max_length=250)
    show_host   = models.ForeignKey('auth.User')

    def __str__(self):
        return self.show_name
    class Meta:
        db_table = 'sm_show'
        ordering    = ['show_date']

class act(models.Model):
    performer       = models.ForeignKey('auth.User')
    show_name       = models.ForeignKey('show')
    song            = models.CharField(max_length=255, blank=False, default="undecided")
    introducer      = models.ForeignKey('auth.User', related_name="introducer", blank=True,  null=True)
    kitten_id       = models.ForeignKey('auth.User', related_name="kitten_id", blank=True, null=True)
    order           = models.IntegerField(blank=False, default="100")
    act_intro       = models.TextField(blank=True)
    stage_prep      = models.TextField(blank=True)
    music_sent      = models.BooleanField(default=False)
    act_notes       = models.TextField(blank=True)
    lighting_notes  = models.TextField(blank=True)
    start_onstage    = models.BooleanField(default=False)
    is_featured     = models.BooleanField(default=False)

    #def __unicode__(self):
    #    return u'%s %s %s %s %s' % (self.song, self.user, self.introducer, self.kitten_id, self.show_name)

    class Meta:
        db_table     = 'sm_act'
        ordering    = ['show_name', 'order']
