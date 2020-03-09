from bs4 import BeautifulSoup as bs
import datetime


def extract(filename):
    with open(filename) as file:
        soup = bs(file, features="html.parser")

    timetable_html = soup.find(id="j_id119:gradeHorarios")
    classes_html =  timetable_html.find_all("textarea", {"class": "campo"})
    time_html = timetable_html.find_all("td", {"class": "horario"})
    infotable_html = soup.find(id="j_id119:j_id324")

    keys = [x for x in range(0, 6)]
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    weekdays = ["MO", "TU", "WE", "TH", "FR", "SA", "SU"]

    key2day = dict(zip(keys, days))
    day2key = dict(zip(days, keys))
    day2abrev = dict(zip(days, weekdays))

    daily_events = {k: [] for k in days}
    class_code = {k: [] for k in keys}
    class_time = [time.contents[0] for time in time_html]

    aux = len(class_time)
    time_counter = 0
    for idx, text in enumerate(classes_html):
        if text.contents != []:
            code, place = text.contents[0].split('\n')
            class_code[idx % 6].append((class_time[time_counter], code, place))
        if idx % 6 == 5:
            time_counter += 1

    infos = infotable_html.find_all("td", {"class": "linha_tabela"})
    code2name = {}
    end = len(infos)
    for idx in range(0, end, 4):
        code = infos[idx].contents[0]
        name = infos[idx + 2].contents[0]
        code2name[code] = name

    for key, classes in class_code.items():
        daily_events[key2day[key]] = extract_periods(classes)

    return daily_events, day2abrev, day2key, code2name


def build_interval(begin, end, code, place):
    end_h, end_m = end.split(":")
    end = datetime.timedelta(hours=int(end_h), minutes=int(end_m)) + datetime.timedelta(minutes=50)
    return ((begin, str(end)), code, place)

def extract_periods(classes):
    l = len(classes)
    intervals = []
    begin_aux = 0
    end_aux = 0
    for x in range(1, l):
        if classes[x - 1][1] == classes[x][1]:
            end_aux = x
        else:
            intervals.append(build_interval(classes[begin_aux][0], classes[end_aux][0], classes[begin_aux][1], classes[begin_aux][2]))
            begin_aux = x
            end_aux = x
        if x == l - 1:
            end_aux = x
            intervals.append(build_interval(classes[begin_aux][0], classes[end_aux][0], classes[begin_aux][1], classes[begin_aux][2]))
    return intervals


def extractor(filename):
    return extract(filename)
