from datetime import datetime
#1
today = datetime.datetime.now()
f_days = datetime.timedelta(days=5)
print(today - f_days)
#2
today2 = datetime.datetime.now()
tomorrow = today2 + (datetime.timedelta(days=1))
yesturday = today2 - (datetime.timedelta(days=1))
print(yesturday,today2,tomorrow)
#3
now = datetime.now()
now_without_ml = now.replace(microsecond=0)
print(now_without_ml)
#4
date1 = datetime(2023, 10, 1, 12, 0, 0)
date2 = datetime(2023, 10, 2, 14, 30, 0)
difference = date2 - date1
seconds = difference.total_seconds()
print(f"Разница в секундах: {seconds} сек.")