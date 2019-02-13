from django.db import models
from django.urls import reverse


SHIFTTIME = (
        ('dayshift', 'day'),
        ('nightshift', 'night'),
)


class Shifter(models.Model):
    employee = models.CharField(max_length=200)
    shift = models.CharField(max_length=15, choices=SHIFTTIME)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    @property
    def get_html_url(self):
        url = reverse('schedule_edit', args=(self.id,))
        return f'<a href="{url}"> {self.employee} </a>'

    def __str__(self):
        return f'{self.employee} on {self.start_time}'
