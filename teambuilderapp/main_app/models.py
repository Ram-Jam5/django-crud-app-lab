from django.db import models

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()

    def __str__(self):
        return self.name
    
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