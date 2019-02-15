from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


TEAM_CHOICES = (
            ('team1', 'Manchester United'),
            ('team2', 'Real Madrid'),
            ('team3', 'Barcelona'),
            ('team4', 'Bayern Munich'),
            ('team5', 'Liverpool'),
            ('team6', 'Juventus'),
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
