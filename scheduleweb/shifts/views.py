from django.shortcuts import render, get_object_or_404
from datetime import datetime, timedelta, date
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.utils.safestring import mark_safe
import calendar

from .models import *
from .customcalendar import Calendar
from .forms import ShifterForm


class CalendarView(generic.ListView):
    model = Shifter
    template_name = 'shifts/mainpage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context

def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month

def schedule(request, schedule_id=None):
    instance = Shifter()
    if schedule_id:
        instance = get_object_or_404(Shifter, pk=schedule_id)
    else:
        instance = Shifter()

    form = ShifterForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('mainpage'))
    return render(request, 'shifts/schedule.html', {'form': form})
