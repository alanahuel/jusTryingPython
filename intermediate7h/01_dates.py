## DATES ##

def new_line():
    print("\n")
def line():
    print("--------------------------------")
    
from datetime import datetime

now = datetime.now()

def print_date(date):
    print(date.year)
    print(date.month)
    print(date.hour)
    print(date.minute)
    print(date.second)
    
print_date(now)

print(now.year)
print(now.month)
print(now.hour)
print(now.minute)
print(now.second)


timestamp = now.timestamp()

print(timestamp)

year_2023 = datetime(2023, 10, 24)

line()

from datetime import time

current_time = time(21, 6, 0)

print(current_time.hour)
print(current_time.minute)
print(current_time.second)

line()

from datetime import date

current_date = date(2023, 7, 27)
current_date_today = date.today()

print(current_date.day)
print(current_date.month)
print(current_date.year)

print(current_date_today)

line()

diff = now - year_2023
print(diff)

line()

from datetime import timedelta

start_timedelta = timedelta(200, 10, 1000, weeks= 10)
end_timedelta = timedelta(300, 1000, 100, weeks=14)
print(end_timedelta - start_timedelta)
print(end_timedelta + start_timedelta)