import datetime

#--------FIRST--------#
curDate = datetime.date.today()
timeDiff = datetime.timedelta(days=5)
print(curDate - timeDiff)

#--------SECOND--------#
curDate = datetime.date.today()
timeDiff = datetime.timedelta(days=1)
print("Yesterday: ", curDate - timeDiff)
print("Today: ", curDate)
print("Tomorrow: ", curDate + timeDiff)

#--------THIRD--------#
curDate = datetime.datetime.today().replace(microsecond=0)
print(curDate)

#--------FOURTH--------#
date1 = datetime.datetime(year=2023, day=15, month=6)
date2 = datetime.datetime(year=2015, day=20, month=9)

timeDiff = date1 - date2
print(timeDiff.total_seconds())