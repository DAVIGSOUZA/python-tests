import datetime as dt
import pytz

print(dt.date(2020,4,22))

print(dt.date.today())

print(dt.date.today().year)

print(dt.date.today().month)

print(dt.date.today().day)

# weekday returns a int
# weekday: segunda = 0 | domingo = 6
print(dt.date.today().weekday())

# iso weekday: segunda = 1 | domingo = 7
print(dt.date.today().isoweekday())


# intervalo de tempo:
today_date = (dt.date.today())

time_delta = (dt.timedelta(days = 12))

print(today_date + time_delta)

# tempo restante
aniversario = dt.date(2022,6,20)

days_left = aniversario - today_date

print(days_left)
print(days_left.days)
print(days_left.total_seconds())


today_time = dt.time(8,30,20,100000)
print(today_time)
print(today_time.hour)
print(today_time.minute)
print(today_time.second)
print(today_time.microsecond)

date_time = dt.datetime(2021,10,4,14,38,22,100000)
print(date_time)
print(date_time.year)
print(date_time.day)
print(date_time.month)
print(date_time.hour)

print(date_time + time_delta)

hour_delta = dt.timedelta(hours = 20)

print(date_time + hour_delta)


dt_today = dt.datetime.today()
print(dt_today)

dt_now = dt.datetime.now()
print(dt_now)

dt_utc = dt.datetime.utcnow()
print(dt_utc)



date_timezone = dt.datetime(2021,10,4,14,48,35,tzinfo = pytz.UTC)
print(date_timezone)