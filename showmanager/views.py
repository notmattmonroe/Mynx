from django.shortcuts import render_to_response, get_object_or_404
from django.views import generic
from .models import show, act
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.template import RequestContext

#def index(request):

    #shows_list = show.objects.all().order_by('-date')
    #return render_to_response('shows/shows_list.html', {'shows_list': shows_list})
    #return render_to_response('base.html', context_instance = RequestContext(request))

class index(generic.ListView):
    template_name = 'showmanager/index.html'
    context_object_name = 'show_list'

    def get_queryset(self):
        return show.objects.order_by('show_date')[:25]



#@login_required
#def performer_detail(request, id):
#    return list_detail.object_detail(
#        request,
#        queryset = performer.objects.all(),
#    )
#    performer_detail.__doc__ = list_detail.object_detail.__doc__

#@login_required
#def performer_list(request):
#    return list_detail.object_list(
#        request,
#        queryset = performer.objects.all(),
#    )
#    performer_list.__doc__ = list_detail.object_list.__doc__

#def show_detail(request, id):
#    return list_detail.object_detail(
#        request,
#        queryset = show.objects.all(),
#        object_id = id,
#    )
#    show_detail.__doc__ = list_detail.object_detail.__doc__
class show_detail(generic.DetailView):
#    pass
    model = show
    template_name = 'showmanager/show_detail.html'



def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/musiclib')


