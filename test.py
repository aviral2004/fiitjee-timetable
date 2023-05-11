from gcsa.google_calendar import GoogleCalendar
from beautiful_date import *
calendar = GoogleCalendar('aviralg1975@gmail.com', './credentials.json')
for event in calendar:
    print(event)

from gcsa.event import Event
event = Event(
    'Class',
    start=(9 / Nov / 2020)[9:00],
    minutes_before_email_reminder=50
)

calendar.add_event(event)

for event in calendar:
    print(event)