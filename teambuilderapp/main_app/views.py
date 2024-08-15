from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Player
# Create your views here.


def home(request):
    return render(request,'home.html')

def player_index(request):
    players = Player.objects.all()
    return render(request, 'player_index.html', {'players': players})

def player_detail(request, player_id):
    player = Player.objects.get(id=player_id)
    return render(request, 'player/detail.html', {'player': player})

class PlayerCreate(CreateView):
    model = Player
    fields = '__all__'

class PlayerUpdate(UpdateView):
    model = Player
    fields = '__all__'

class PlayerDelete(DeleteView):
    model = Player
    success_url = '/players/'
