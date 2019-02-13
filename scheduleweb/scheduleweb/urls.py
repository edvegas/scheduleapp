from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('superadm/', admin.site.urls),
    path('', include('authorization.urls')),
    path('', include('shifts.urls')),
]
