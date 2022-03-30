from datetime import datetime
from datetime import time
from datetime import timedelta
from datetime import date
import locale

d1 = date(2019, 3, 12)
print(d1)
print(d1.year)
print(d1.month)
print(d1.day)

t1 = time(23, 10, 59)
print(t1.hour)
print(t1.minute)
print(t1.second)

print(date.today)
print(date.max)
print(date.min)

dt = datetime(2019, 3, 12, 15, 17)
print(dt)

print(dt.date().year)
print(dt.time().hour)
print(datetime.max)

print(datetime.now())

new_dt = datetime.now().replace(year=2018)
print(new_dt)

dt = datetime.strptime("30/08/2022 10:49", "%d/%m/%Y %H:%M")
print(dt)

dt = datetime.strptime("06-28-2052 10:49", "%m-%d-%Y %H:%M")
print(dt)

dt = datetime.strptime("2018-02-26", "%Y-%m-%d")
print(dt.year, dt.month, dt.day)

locale.setlocale(locale.LC_ALL, "")
print(locale.setlocale(locale.LC_ALL, ""))

now = datetime.now()
print(now.strftime("%Y-%m-%d (%a)"))
print(now.strftime("%Y-%B-%d число '%A'"))

delta1 = timedelta(days=3, hours=2, minutes=10)
print(delta1)

delta2 = timedelta(days=2, hours=1, minutes=5)
print(delta2 - delta1)
print(delta1 - delta2)

my_birthday = date(1985, 10, 2)
print(my_birthday)

delta = date.today() - my_birthday
print(delta)

my_age = int(delta.days / 365)
print(my_age)


