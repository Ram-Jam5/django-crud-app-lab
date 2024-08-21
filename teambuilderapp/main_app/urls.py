from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('players/', views.player_index, name='player-index'),
    path('players/<int:player_id>/', views.player_detail, name='player-detail'),
    path('players/create/', views.PlayerCreate.as_view(), name='player-create'),
    path('players/<int:pk>/update/', views.PlayerUpdate.as_view(), name='player-update'),
    path('players/<int:pk>/delete/', views.PlayerDelete.as_view(), name='player-delete'),
    path('rating/create', views.RatingCreate.as_view(), name='rating-create'),
    path('rating/<int:pk>/', views.RatingDetail.as_view(), name='rating-detail'),
    path('rating/', views.RatingList.as_view(), name='rating-index'),
    path('rating/<int:pk>/update/', views.RatignUpdate.as_view(), name='rating-update'),
    path('rating/<int:pk>/delete/', views.RatingDelete.as_view(), name='rating-delete'),
    path('rating/<int:pk>/associate-rating/<int:rating_id>/', views.associate_rating, name='associate-rating')
]