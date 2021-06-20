from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('calendar/', views.resources, name='calender'),
    path('alarms/', views.meetings, name='alarms'),
    path('newevent/', views.newMeeting, name='newevent'),
    path('newentry/', views.newEvent, name='newentry'),
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),
]
