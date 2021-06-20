from django.shortcuts import render, get_object_or_404
from .models import Calendar, Alarms, Entries, Event
from django.urls import reverse_lazy
from .forms import MeetingForm, EventForm, ResourceForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    return render(request, 'lamp/index.html')

def calendar(request):
    calendar_list=Resource.objects.all()
    return render(request, 'lamp/calendar.html', {'calendar_list' : calendar_list})

def alarms(request):
    alarms_list=Meeting.objects.all()
    return render(request, 'lamp/newalarm.html', {'alarms_list' : alarms_list})

def entries(request, id):    
    entries_view=get_object_or_404(Meeting, pk=id)
    return render(request, 'lamp/newentry.html', {'entries_view': entries_view})

def event(request, id):    
    event_view=get_object_or_404(Meeting, pk=id)
    return render(request, 'club/newevent.html', {'event_view': event_view})

#forms 
@login_required
def newMeeting(request):
    form=MeetingForm

    if request.method=='POST':
        form=MeetingForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=MeetingForm()
    else:
        form=MeetingForm()
    return render(request, 'club/newmeeting.html', {'form': form})

@login_required
def newResource(request):
    form=ResourceForm

    if request.method=='POST':
        form=ResourceForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=ResourceForm()
    else:
        form=ResourceForm()
    return render(request, 'club/newresource.html', {'form': form})

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


# login view

def loginmessage(request):
    return render(request, 'club/loginmessage.html')

# logout view

def logoutmessage(request):
    return render(request, 'club/logoutmessage.html')