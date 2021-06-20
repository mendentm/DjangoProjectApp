from django import forms
from .models import Calendar, Alarms, Event, Entries

class CalendatrForm(forms.ModelForm):
    class Meta:
        model=Calendar
        fields='__all__'

class AlarmsForm(forms.ModelForm):
    class Meta:
        model=Alarms
        fields='__all__'

class EventForm(forms.ModelForm):
    class Meta:
        model=Event
        fields='__all__'

class EntriesForm(forms.ModelForm):
    class Meta:
        model=Entries
        fields='__all__'

