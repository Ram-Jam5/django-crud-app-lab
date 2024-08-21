from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Player, Rating
from .forms import TrophyForm
from django.views.generic import ListView, DetailView
# Create your views here.


def home(request):
    return render(request,'home.html')

def player_index(request):
    players = Player.objects.all()
    return render(request, 'player_index.html', {'players': players})

def player_detail(request, player_id):
    player = Player.objects.get(id=player_id)
    rating = Rating.objects.all()
    trophy_form = TrophyForm()
    return render(request, 'player/detail.html', {'player': player, 'trophy_form': trophy_form, 'rating':rating })

class PlayerCreate(CreateView):
    model = Player
    fields = '__all__'

class PlayerUpdate(UpdateView):
    model = Player
    fields = '__all__'

class PlayerDelete(DeleteView):
    model = Player
    success_url = '/players/'
    
class RatingCreate(CreateView):
    model = Rating
    fields = '__all__'
    
class RatingList(ListView):
    model = Rating
    
class RatingDetail(DetailView):
    model = Rating
    
class RatingUpdate(UpdateView):
    model = Rating
    fields = '__all__'
    
class RatingDelete(DeleteView):
    model = Rating
    success_url = '/rating/'
    
def associate_rating(request, player_id, rating_id):
    Player.objects.get(id=player_id).rating.add(rating_id)
    return redirect('player-detail', player_id=player_id)