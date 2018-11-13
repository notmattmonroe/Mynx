from django.contrib import admin
from .models import Course, Session

class CourseAdmin(admin.ModelAdmin):
    list_display = ("course_name", "instructor", "is_active",)
    list_editable = ("instructor", "is_active",)
    prepopulated_fields = {"slug": ("session_id","course_name",)}
    fieldsets = [
        (None,               {'fields': ['session_id','course_name', 'slug', 'instructor', 'category', 'description', 'is_workshop','image']}),
        ('Date information', {'fields': ['start_time', 'end_time', 'days_of_week', 'all_day', 'custom_start_date', 'custom_end_date', 'publish_date', 'is_active']}),
        ('Logistics', {'fields': ['is_private', 'spaces', 'price', 'dropins', 'dropin_price', 'location', 'ticket_link']}),
    ]

admin.site.register(Course, CourseAdmin)
admin.site.register(Session)


