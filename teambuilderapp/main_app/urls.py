from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('players/', views.player_index, name='player-index'),
    path('players/<int:player_id>/', views.player_detail, name='player-detail'),
]