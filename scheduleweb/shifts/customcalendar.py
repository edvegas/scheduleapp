from datetime import datetime, timedelta
from calendar import HTMLCalendar
from .models import Shifter


class Calendar(HTMLCalendar):
    
    def __init__(self, year=None, month=None):
        self.year = year
        self.month = month
        super(Calendar, self).__init__()

    def formatday(self, day, schedules):
        schedules_per_day = schedules.filter(start_time__day=day)
        d = ''
        for schedule in schedules_per_day:
            d += f'<li> {schedule.get_html_url} </li>'

        if day != 0:
            return f"<td><span class='date'>{day}</span><ul> {d} </ul></td>"
        return '<td></td>'

    def formatweek(self, theweek, schedules):
        week = ''
        for d, weekday in theweek:
            week += self.formatday(d, schedules)
        return f'<tr> {week} </tr>'

    def formatmonth(self, withyear=True):
        schedules = Shifter.objects.filter(start_time__year=self.year, start_time__month=self.month)
        cal = f"<table border='0' cellpadding='0' cellspacing='0' class='calendar'>\n"
        cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
        cal += f'{self.formatweekheader()}\n'
        for week in self.monthdays2calendar(self.year, self.month):
            cal += f'{self.formatweek(week, schedules)}\n'
        return cal
