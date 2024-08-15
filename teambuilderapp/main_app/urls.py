from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('players/', views.player_index, name='player-index'),
    path('players/<int:player_id>/', views.player_detail, name='player-detail'),
    path('players/create/', views.PlayerCreate.as_view(), name='player-create'),
    path('players/<int:pk>/update/', views.PlayerUpdate.as_view(), name='player-update'),
    path('players/<int:pk>/delete/', views.PlayerDelete.as_view(), name='player-delete'),
]