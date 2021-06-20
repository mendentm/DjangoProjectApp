from django.shortcuts import render, get_object_or_404
from .models import Calendar, Alarms, Entries, Event
from django.urls import reverse_lazy
from .forms import CalendarForm, EventForm, AlarmsForm, EntriesForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    return render(request, 'lamp/index.html')

def calendar(request):
    calendar_list=Calendar.objects.all()
    return render(request, 'lamp/index.html', {'calendar_list' : calendar_list})

def alarms(request):
    alarms_list=Alarms.objects.all()
    return render(request, 'lamp/newalarm.html', {'alarms_list' : alarms_list})

def entries(request):    
    entries_list=Entries.objects.all()
    return render(request, 'lamp/newentry.html', {'entries_list': entries_list})

def event(request, id):    
    event_view=get_object_or_404(Event, pk=id)
    return render(request, 'club/newevent.html', {'event_view': event_view})

#forms 
@login_required
def new_calendar_form(request):
    form=CalendarForm

    if request.method=='POST':
        form=CalendarForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=CalendarForm()
    else:
        form=CalendarForm()
    return render(request, 'lamp/calendar.html', {'form': form})

@login_required
def newAlarms(request):
    form=AlarmsForm

    if request.method=='POST':
        form=AlarmsForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=AlarmsForm()
    else:
        form=AlarmsForm()
    return render(request, 'club/newalarm.html', {'form': form})

@login_required
def newEvent(request):
    form=EventForm

    if request.method=='POST':
        form=EventForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=EventForm()
    else:
        form=EventForm()
    return render(request, 'club/newevent.html', {'form': form})


@login_required
def newentry(request):
    form=EntriesForm

    if request.method=='POST':
        form=EntriesForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=EntriesForm()
    else:
        form=EntriesForm()
    return render(request, 'club/newentry.html', {'form': form})



# login view

def loginmessage(request):
    return render(request, 'club/loginmessage.html')

# logout view

def logoutmessage(request):
    return render(request, 'club/logoutmessage.html')