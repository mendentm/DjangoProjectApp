from django.contrib import admin
from .models import Calendar, Alarms, Event, Entries
# Register your models here.
admin.site.register(Calendar)
admin.site.register(Alarms)
admin.site.register(Event)
admin.site.register(Entries)


', views.index, name='index'),
    path('calendar/', views.calendar, name='calender'),
    path('alarms/', views.alarms, name='alarms'),
    path('newevent/', views.newevent, name='newevent'),
    path('newentry/', views.newentry, name='newentry'),
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),
]