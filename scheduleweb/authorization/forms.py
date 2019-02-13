from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


TEAM_CHOICES = (
            ('team1', 'PBB/ LCP/ Husqvarna/ GESS'),
            ('team2', 'RenCap/ BAT/ Schiphol'),
            ('team3', 'DKSS/ Kering/ MBF'),
            ('team4', 'Bridgestone JS/ Mazda/ British Council'),
            ('team5', 'Operating ITG'),
            ('team6', 'Operating Bridgestone/DKSS'),
)


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=50)
    
    phone = forms.RegexField(
            regex=r'^\+79\d{9,15}$',
            widget=forms.TextInput(attrs={'placeholder': 'Format: +79xxxxxxxxx, up to 15 digits'}),
    )

    team = forms.CharField(
        max_length=30,
        widget=forms.Select(choices=TEAM_CHOICES),
    )

    class Meta:
        model = User
        fields = ('username', 
                  'password1', 
                  'password2', 
                  'first_name', 
                  'last_name', 
                  'email', 
                  'phone', 
                  'team')


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(max_length=50)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('phone',)
