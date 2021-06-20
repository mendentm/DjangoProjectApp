from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('calendar/', views.calendar, name='calender'),
    path('alarms/', views.alarms, name='alarms'),
    path('newevent/', views.event, name='newevent'),
    path('newentry/', views.entries, name='newentry'),
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),
]
