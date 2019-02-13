from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
       path('', login_required(views.CalendarView.as_view()), name='mainpage'),
       path('schedule/new/', views.schedule, name='schedule_new'),
       path('schedule/edit/<int:schedule_id>/', views.schedule, name='schedule_edit'),
]
