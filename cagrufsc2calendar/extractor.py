from constants import key2day, keys, WEEKDAYS
from bs4 import BeautifulSoup as bs
import datetime


def extract(filename):
    with open(filename) as file:
        soup = bs(file, features="html.parser")

    classes_html =  soup.find_all("textarea", {"class": "campo"})
    time_html = soup.find_all("td", {"class": "horario"})
    infos = soup.find_all("td", {"class": "linha_tabela"})




    daily_events = {k: [] for k in WEEKDAYS}
    class_code = {k: [] for k in keys}
    class_time = [time.contents[0] for time in time_html]


    code2name = {}
    end = len(infos)
    for idx in range(0, end, 4):
        code = infos[idx].contents[0]
        name = infos[idx + 2].contents[0]
        code2name[code] = name

    aux = len(class_time)
    time_counter = 0
    for idx, text in enumerate(classes_html):
        if text.contents != []:
            code, place = text.contents[0].split('\n')
            code = code.split("-")[0]
            class_code[idx % 6].append((class_time[time_counter], code2name[code], code, place))
        if idx % 6 == 5:
            time_counter += 1



    for key, classes in class_code.items():
        daily_events[key2day[key]] = extract_periods(classes)


    return daily_events


def build_interval(begin, end, name, code, place):
    end_h, end_m = end.split(":")
    end = datetime.timedelta(hours=int(end_h), minutes=int(end_m)) + datetime.timedelta(minutes=50)
    return ((begin, str(end)), name, code, place)

def extract_periods(classes):
    l = len(classes)
    intervals = []
    begin_aux = 0
    end_aux = 0
    for x in range(1, l):
        if classes[x - 1][1] == classes[x][1]:
            end_aux = x
        else:
            intervals.append(build_interval(classes[begin_aux][0], \
                                            classes[end_aux][0],   \
                                            classes[begin_aux][1], \
                                            classes[begin_aux][2], \
                                            classes[begin_aux][3]))
            begin_aux = x
            end_aux = x
        if x == l - 1:
            end_aux = x
            intervals.append(build_interval(classes[begin_aux][0], \
                                            classes[end_aux][0],   \
                                            classes[begin_aux][1], \
                                            classes[begin_aux][2], \
                                            classes[begin_aux][3]))
    return intervals


def extractor(filename):
    return extract(filename)
