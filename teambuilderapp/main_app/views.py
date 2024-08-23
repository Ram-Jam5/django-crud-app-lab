from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Player, Rating
from .forms import TrophyForm
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class Home(LoginView):
    template_name = 'home.html'

@login_required
def player_index(request):
    players = Player.objects.filter(user=request.user)
    return render(request, 'player_index.html', {'players': players})

@login_required
def player_detail(request, player_id):
    player = Player.objects.get(id=player_id)
    rating = Rating.objects.all()
    trophy_form = TrophyForm()
    return render(request, 'player/detail.html', {'player': player, 'trophy_form': trophy_form, 'rating':rating })

class PlayerCreate(LoginRequiredMixin, CreateView):
    model = Player
    fields = ['name', 'team', 'player_position', 'description', 'age', 'profile_image', 'rating']
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
class PlayerUpdate(LoginRequiredMixin, UpdateView):
    model = Player
    fields = ['name', 'team', 'player_position', 'description', 'age', 'profile_image', 'rating']

class PlayerDelete(LoginRequiredMixin, DeleteView):
    model = Player
    success_url = '/players/'
    
class RatingCreate(LoginRequiredMixin, CreateView):
    model = Rating
    fields = '__all__'
    
class RatingList(LoginRequiredMixin, ListView):
    model = Rating
    
class RatingDetail(LoginRequiredMixin, DetailView):
    model = Rating
    
class RatingUpdate(LoginRequiredMixin, UpdateView):
    model = Rating
    fields = '__all__'
    
class RatingDelete(LoginRequiredMixin, DeleteView):
    model = Rating
    success_url = '/rating/'
    
def associate_rating(request, player_id, rating_id):
    Player.objects.get(id=player_id).rating.add(rating_id)
    return redirect('player-detail', player_id=player_id)


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('player-index')
        else:
            error_message = 'Invalid sign up - try again'
    form =UserCreationForm()
    context = {'form':form, 'error_message':error_message}
    return render(request, 'signup.html', context)