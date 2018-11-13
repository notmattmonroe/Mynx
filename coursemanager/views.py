from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
#from django.conf.urls import reverse
from django.views import generic
from .models import Course, Session


class IndexView(generic.ListView):
    template_name = 'coursemanager/index.html'
    context_object_name = 'latest_courses_list'

    def get_queryset(self):
        """Return the last five published courses."""
        return Course.objects.filter(isActive=True).order_by('category_id','course_name')[:30]
    
    
class DetailView(generic.DetailView):
    model = Course
    #courserecur = Course.objects.get(pk=1)
    #text_rules_inclusion = []

    #for rule in courserecur.course_recurring.rrules:
     #   text_rules_inclusion.append(rule.to_text())
    
    template_name = 'coursemanager/detail.html'

