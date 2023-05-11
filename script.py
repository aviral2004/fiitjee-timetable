import requests
from bs4 import BeautifulSoup

URL = "http://fiitjeenorthwest.com/time_table.php"
args= {'batch': 'NWCM2022X1W', 'submit': 'Submit'}

page = requests.post(URL, data = args)
soup = BeautifulSoup(page.content, 'html.parser')

week = []

table = soup.find(class_='banner_flash1_mid_DATADATA').find_all('table')[3].find_all('tr')
for i in table[0].find_all('td'):
    current_date = i.text.split('\n')[1][1:-1]
    week.append({'date': current_date, 'classes': []})

for i in table[1:]:
    cells = i.find_all('td')
    for i in range(len(cells)):
        if cells[i].text != '':
            week[i]['classes'].append(cells[i].text)

teachers = {'MSV2': 'Maths Class', 'CSN2': 'Chemistry Class', 'PBK4': 'Physics Class'}

from gcsa.google_calendar import GoogleCalendar
from beautiful_date import *
from datetime import datetime
from gcsa.event import Event
calendar = GoogleCalendar('aviralg1975@gmail.com', './credentials.json')
for event in calendar:
    print(event)

for day in week:
    for clss in day['classes']:
        if len(clss.split('\n')) > 1:
            name, timing = clss.split('\n')
            date = list(map(int, day['date'].split('/'))) # In the format 11/12/2020
            start, end = timing.split('-') # In the format 10:30-12:00
            start_time = datetime(day=date[0], month=date[1], year=date[2], hour=int(start.split(':')[0]), minute=int(start.split(':')[1]))
            end_time = datetime(day=date[0], month=date[1], year=date[2], hour=int(end.split(':')[0]), minute=int(end.split(':')[1]))
            if name in teachers:
                event = Event(
                    teachers[name],
                    start=start_time,
                    end=end_time
                )
                calendar.add_event(event)
            else:
                event = Event(
                    name,
                    start=start_time,
                    end=end_time
                )
                calendar.add_event(event)
            print('Adding:', name, start_time, end_time)

for event in calendar:
    print(event)