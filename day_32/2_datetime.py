import datetime as dt

now=dt.datetime.now()
year=now.year
month=now.month
day_of_week=now.weekday ()
# monday=1
# tuesday=2

if year==2022:
    print("wear your mask.")
print(day_of_week)

date_of_birth=dt.datetime(year=2005,month=3,day=19,hour=9)
print(day_of_week)