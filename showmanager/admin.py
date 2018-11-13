from showmanager.models import show, act
from django.contrib import admin

class show_admin(admin.ModelAdmin):
        list_display = ("show_name", "show_date", "show_host",)

class act_admin(admin.ModelAdmin):
	list_display = ("song", "show_name", "performer", "introducer", "kitten_id", "order", "music_sent",)

#	def show_name(self, obj):
#	    return obj.show.show_name

admin.site.register(show, show_admin)
admin.site.register(act, act_admin)

