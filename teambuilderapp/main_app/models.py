from django.db import models
from django.urls import reverse
from datetime import date
# Import the User
from django.contrib.auth.models import User
# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()

    def __str__(self):
        return self.name

class Rating(models.Model):
    rating = models.CharField(max_length=200)
    sell = models.CharField(max_length=50)
    
    def __str__(self):
        return self.rating
    def get_absolute_url(self):
        return reverse("rating-detail", kwargs={"pk": self.id})        
class Player(models.Model):
    name = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    STRIKER = "ST"
    LEFT_WING = "LW"
    RIGHT_WING = "RW"
    ATTACKING_MIDFIELDER = "AM"
    DEFENSIVE_MIDFIELDER = "DM"
    LEFT_BACK = "LB"
    CENTER_BACK = "CB"
    RIGHT_BACK = "RB"
    GOAL_KEEPER = "GK"
    PLAYER_POSITION_CHOICES = {
        "ST": "Striker",
        "LW": "Left Wing",
        "RW": "Right Wing",
        "AM": "Attacking Midfielder",
        "DM": "Defensive Midfielder",
        "LB": "Left Back",
        "CB": "Center Back",
        "RB": "Right Back",
        "GK": "Goal Keeper",
    }
    player_position = models.CharField(
        max_length=2,
        choices=PLAYER_POSITION_CHOICES,
        default=STRIKER,
    )
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    profile_image = models.ImageField(upload_to='images/player_images/', blank=True, null=True)
    rating = models.ManyToManyField(Rating)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.name
    
    def is_attacker(self):
        return self.player_position in {self.STRIKER, self.LEFT_WING, self.RIGHT_WING}
    
    def is_midfielder(self):
        return self.player_position in {self.ATTACKING_MIDFIELDER, self.DEFENSIVE_MIDFIELDER}
    
    def is_defender(self):
        return self.player_position in {self.RIGHT_BACK, self.LEFT_BACK, self.CENTER_BACK}
    def is_goalkeeper(self):
        return self.player_position in {self.GOAL_KEEPER}
    
    def get_absolute_url(self):
        return reverse('player-detail', kwargs={'player_id': self.id})

TROPHIES =(
    ('EPL', 'English Premier League'),
    ('UCL', 'UEFA Champions League'),
    ('FAC', 'Footballers Association Cup'),
    ('NON','No Trophies won this season!'),
    )
class Trophy(models.Model):
    date = models.DateField('Trophy Date')
    trophy = models.CharField(
        max_length=3,
        choices = TROPHIES,
        default=TROPHIES[3][0]
    )
    
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.get_trophy_display()}"
    

    