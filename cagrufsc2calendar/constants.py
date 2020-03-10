WEEKDAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
WEEKDAYS_ABREV = ["MO", "TU", "WE", "TH", "FR", "SA", "SU"]
keys = [x for x in range(0, 6)]

key2day = dict(zip(keys, WEEKDAYS))
day2key = dict(zip(WEEKDAYS, keys))
day2abrev = dict(zip(WEEKDAYS, WEEKDAYS_ABREV))
