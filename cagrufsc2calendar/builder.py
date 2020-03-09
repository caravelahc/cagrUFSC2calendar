from icalendar import Calendar, Event, vRecur
import pytz
import datetime

def next_day(given_date, weekday):
    day_shift = (weekday - given_date.weekday()) % 7
    return given_date + datetime.timedelta(days=day_shift)

def build_calendar(daily_events, day2abrev, day2key, code2name, end_date, repeat):

    end_grad = datetime.datetime.strptime(end_date, '%Y-%m-%d')


    cal = Calendar()

    now = datetime.datetime.now()
    year = now.year
    month = now.month
    weekday = now.day

    days_left = end_grad - now
    if not repeat:
        weeks_left = int(days_left.days / 7) + 1
    else:
        weeks_left = int(repeat) + 1

    for day, events in daily_events.items():
        next_day = now + datetime.timedelta(days=(day2key[day] - now.weekday()) % 7)
        next_day = next_day.day
        for ev in events:
            if ev:
                event = Event()
                begin = ev[0][0]
                end = ev[0][1]
                description = ev[1].split("-")[0]
                title = code2name[description]
                place = ev[2]
                event.add('summary', title)
                event.add('location', place)
                event.add('description', description)
                begin_hour, begin_minute = begin.split(":")
                end_hour, end_minute, end_second = end.split(":")

                event.add('dtstart', datetime.datetime(year, month, next_day, \
                          hour=int(begin_hour), minute=int(begin_minute)))
                event.add('dtend', datetime.datetime(year, month, next_day,  \
                          hour=int(end_hour), minute=int(end_minute)))
                event['RRULE'] = vRecur({'COUNT': [weeks_left], \
                                        'FREQ': ['WEEKLY'], \
                                        'BYDAY': day2abrev[day]})
                cal.add_component(event)
    return cal

def save_file(output, calendar):
    output_file = output + '.ics'
    print("Saving file to", output_file, '...')
    with open(output_file, 'wb') as file:
        file.write(calendar.to_ical())
    print("Done!")
def build(OUTPUT, END_DATE, REPEAT, daily_events, day2abrev, day2key, code2name):
    calendar = build_calendar(daily_events, day2abrev, day2key, code2name, \
                              END_DATE, REPEAT)
    save_file(OUTPUT, calendar)
