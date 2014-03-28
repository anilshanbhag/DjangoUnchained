from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.forms import ModelForm
from gen2048.models import Game

class GameForm(ModelForm):
    class Meta:
        model = Game
        exclude = ['owner']

def home(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            f = GameForm(request.POST, request.FILES)
            if f.is_valid():
                game = f.save(commit=False)
                game.owner = request.user
                game.save()
                return HttpResponseRedirect('/' + game.url)
            else:
                ctx = {'form': f}
                return render_to_response('setup.html', RequestContext(request,ctx))
        else:
            form = GameForm()
            ctx = {'form': form}
            return render_to_response('setup.html', RequestContext(request,ctx))
    else:
        return HttpResponseRedirect('/admin/')

def game(request, url):
    try:
        game = Game.objects.get(url = url)
        ctx = {'game': game}
        return render_to_response('index.html', RequestContext(request,ctx))
    except Game.DoesNotExist:
        return HttpResponseRedirect('/')