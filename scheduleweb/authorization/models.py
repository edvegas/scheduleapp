from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


TEAM_CHOICES = (
            ('team1', 'PBB/ LCP/ Husqvarna/ GESS'),
            ('team2', 'RenCap/ BAT/ Schiphol'),
            ('team3', 'DKSS/ Kering/ MBF'),
            ('team4', 'Bridgestone JS/ Mazda/ British Council'),
            ('team5', 'Operating ITG'),
            ('team6', 'Operating Bridgestone/DKSS'),
)


class Profile(models.Model):
    
    phone_regex = RegexValidator(regex=r'^\+79\d{9,15}$')

    user = models.OneToOneField(User, on_delete = models.CASCADE)
    phone = models.CharField(validators=[phone_regex], max_length=15, blank=True) 
    team = models.CharField(max_length=30, choices=TEAM_CHOICES)

    def __str__(self):
        return self.user.username
