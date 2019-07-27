import sys
import math
from datetime import datetime, timedelta

def months_between(date1, date2):
    if date1>date2:
        date1,date2=date2,date1
    m1=date1.year*12+date1.month
    m2=date2.year*12+date2.month
    months=m2-m1
    if date1.day>date2.day:
        months-=1
    elif date1.day==date2.day:
        seconds1=date1.hour*3600+date1.minute+date1.second
        seconds2=date2.hour*3600+date2.minute+date2.second
        if seconds1>seconds2:
            months-=1
    return months

date_start = datetime.strptime(input(), '%d.%m.%Y')
date_end = datetime.strptime(input(), '%d.%m.%Y')

diff = date_end-date_start

#diff.days
day = diff.days
year = day//365
month = months_between(date_end, date_start)-12*year

print(day, month, year, file=sys.stderr)

result_arr = []

if year > 1:
    result_arr.append("%s years" % year)
elif year == 1:
    result_arr.append("1 year")
    
if month > 1:
    result_arr.append("%s months" % month)
elif month == 1:
    result_arr.append("1 month")

if day == 0:
    result_arr.append("total 0 days")
elif day == 1:
    result_arr.append("total 1 day")
else:
    result_arr.append("total %s days"% day)


print(", ".join(result_arr))
