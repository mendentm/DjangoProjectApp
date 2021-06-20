from django.test import TestCase
from django.contrib.auth.models import User
from .models import Calendar, Alarms, Entries, Event
import datetime
from django.urls import reverse
from .forms import CalendarForm, AlarmsForm, EntriesForm, EventForm
from django.urls import reverse_lazy, reverse
# Create your tests here.
class CalendarTest(TestCase):
    def setUp(self):
        self.type=Calendar(CalendarTitle='A test text for Calendar')

    def test_typestring(self):
        self.assertEqual(str(self.type), 'A test text for Calendar')

    def test_tablename(self):
        self.assertEqual(str(Calendar._meta.db_table), 'Calendar')

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)


class AlarmsTest(TestCase):
    def setUp(self):
        self.type=Alarms(AlarmsText='Test alarmstext')
        
    def test_tablename(self):
        self.assertEqual(str(Alarms._meta.db_table), 'Test alarmstext')

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
       

class EntriesTest(TestCase):
    def setUp(self):
        self.UserId=User(username='user1')  
        self.Entries=Entries(EntriesType='Entries test', DateEntered=datetime.date(2024,5,17), Description='Entries description')

    def test_string(self):
        self.assertEqual(str(self.Entries), 'Entries test')

    def test_tablename(self):
        self.assertEqual(str(Entries._meta.db_table), 'Entries')
   
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)


class EventTest(TestCase):
    def setUp(self):
        self.type=Event(EventTitle='A test Event')

    def test_typestring(self):
        self.assertEqual(str(self.type), 'A test Event')

    def test_tablename(self):
        self.assertEqual(str(Event._meta.db_table), 'Event')

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)


# form tests

class NewCalendarForm(TestCase):
    #valid form data
    def test_calendarform(self):
        data={

        'CalendarTitle': 'a title test', 
        'Calendardate': '2022-5-8',
        'Calendartext': 'hello',

        }

        form=CalendarForm (data)
        self.assertTrue(form.is_valid)


class NewAlarmsForm(TestCase):
    #valid form data
    def test_resourceform(self):
        data={

        'AlarmId': '10', 
        'ResourceText' : 'nothing',
        }

        form=AlarmsForm (data)
        self.assertTrue(form.is_valid)
 

class NewEventForm(TestCase):
    #valid form data
    def test_eventform(self):
        data={

        'EventTitle': 'executive', 
        'EventLocation' : 'nothing',
        'UserId' : 'david',
        'EventDate': '2020-1-5',
        'EventTime': '4:42:50',
        'EventDescription': 'Anything',

        }

        form=EventForm (data)
        self.assertTrue(form.is_valid)

# Authentication Test

class New_Event_Authentication_Test(TestCase):
    def setUp(self):
        self.test_user=User.objects.create_user(username='testuser1', password='password')
        self.Event=Event.objects.create(EventTitle='Eventtitle test', UserId=self.test_user, EventDate=datetime.date(2021,1,10), EventDescription='Event description')
    
    def test_redirect_if_not_logged_in(self):
        response=self.client.get(reverse('newevent'))
        self.assertRedirects(response, '/accounts/login/?next=/lamp/newevent/')
