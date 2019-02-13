from django.forms import ModelForm, DateInput
from .models import Shifter
from django import forms


SHIFTTIME = (
        ('dayshift', 'day'),
        ('nightshift', 'night'),
)

class ShifterForm(ModelForm):
    class Meta:
        model = Shifter
        shift = forms.CharField(
                        max_length=30,
                        widget=forms.Select(choices=SHIFTTIME),
        )

        widgets = {
            'start_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
            'end_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
        }
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ShifterForm, self).__init__(*args, **kwargs)
        # input_formats to parse HTML5 datetime-local input to datetime field
        self.fields['start_time'].input_formats = ('%Y-%m-%dT%H:%M',)
        self.fields['end_time'].input_formats = ('%Y-%m-%dT%H:%M',)
