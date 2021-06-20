from django.db import models
from django.contrib.auth.models import User

class Calendar(models.Model):
    CalendarTitle=models.CharField(max_length=255)
    CalendarDate=models.DateField()
    CalendarText=models.CharField(max_length=255)

    def __str__(self):
        return self.CalendarTitle

    class Meta:
        db_table='Calendar'

class Alarms(models.Model):
    AlarmsId=models.ForeignKey(User, on_delete=models.CASCADE)
    AlarmsText=models.TextField()

    def __str__(self):
        return self.AlarmsId
    class Meta:
        db_table="Alarms"

class Entries(models.Model):
    EntriesName=models.CharField(max_length=255)
    EntriesType=models.CharField(max_length=255)
    UserId=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    DateEntered=models.DateField()
    Description=models.TextField()

    def __str__(self):
        return self.EntriesName

    class Meta:
        db_table='Entries'

class Event(models.Model):
    EventTitle=models.CharField(max_length=255)
    UserId=models.ForeignKey(User, on_delete=models.CASCADE)
    EventLocation=models.CharField(max_length=255)
    EventDate=models.DateField()
    EventTime=models.TimeField()
    EventDescription=models.CharField(max_length=255)

    def __str__(self):
        return self.EventTitle

    class Meta:
        db_table='Event'    
