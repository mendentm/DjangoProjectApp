from django.contrib import admin
from .models import Calendar, Alarms, Event, Entries
# Register your models here.
admin.site.register(Calendar)
admin.site.register(Alarms)
admin.site.register(Event)
admin.site.register(Entries)

