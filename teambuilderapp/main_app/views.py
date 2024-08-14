from django.shortcuts import render
from .models import Player
# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Hello world</h1>')

def player_index(request):
    players = Player.objects.all()
    return render(request, 'player_index.html', {'players': players})