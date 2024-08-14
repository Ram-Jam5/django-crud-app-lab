from django.shortcuts import render
from .models import Player
# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Hello world</h1>')

def player_index(request):
    players = Player.objects.all()
    return render(request, 'player_index.html', {'players': players})

def player_detail(request, player_id):
    player = Player.objects.get(id=player_id)
    return render(request, 'player/detail.html', {'player': player})