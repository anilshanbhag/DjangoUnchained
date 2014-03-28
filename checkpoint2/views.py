from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect

def home(request):
    if request.user.is_authenticated():
        ctx = {}
        return render_to_response('setup.html', RequestContext(request,ctx))
    else:
        return HttpResponseRedirect('/admin/')
