from datetime import *
#1 current time
x = datetime.datetime.now()
print(x)
# 2 timer
start = datetime.now()
sum(range(10**9))
end = datetime.now()
dif = end-start
print(f"Operation spent around {dif.total_seconds()} second")
# 3 days_timer
def days_until(target_day):
    today = date.today()
    delta = target_day - today
    print(f'It still {delta.days} days before target day ')
tar_day = date(2027,1,1)
days_until(tar_day)
#4 which week days
today = date.today()
which_week_day = today.weekday()
print(which_week_day)
#5 get time atributes
t = date.today()
print(f'{t.year,t.month,t.day}')