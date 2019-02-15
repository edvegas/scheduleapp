from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


TEAM_CHOICES = (
            ('team1', 'Manchester United'),
            ('team2', 'Real Madrid'),
            ('team3', 'Barcelona'),
            ('team4', 'Bayern Munich'),
            ('team5', 'Liverpool'),
            ('team6', 'Juventus'),
)


class Profile(models.Model):
    
    phone_regex = RegexValidator(regex=r'^\+79\d{9,15}$')

    user = models.OneToOneField(User, on_delete = models.CASCADE)
    phone = models.CharField(validators=[phone_regex], max_length=15, blank=True) 
    team = models.CharField(max_length=30, choices=TEAM_CHOICES)

    def __str__(self):
        return self.user.username
