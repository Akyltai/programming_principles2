import sys
import math
import calendar
from datetime import datetime, timedelta

def parse_tz(tz_str):
    sign = 1 if '+' in tz_str else -1
    parts = tz_str.replace('UTC+', '').replace('UTC-', '').split(':')
    return sign * (int(parts[0]) * 60 + int(parts[1]))

def get_utc_time(date_str, offset_minutes):
    y, m, d = map(int, date_str.split('-'))
    local_dt = datetime(y, m, d)
    return local_dt - timedelta(minutes=offset_minutes)

def get_birthday_utc(target_year, b_month, b_day, b_offset):
    m, d = b_month, b_day
    if m == 2 and d == 29 and not calendar.isleap(target_year):
        d = 28
    return datetime(target_year, m, d) - timedelta(minutes=b_offset)

def solve():
    input_data = sys.stdin.read().splitlines()
    if len(input_data) < 2:
        return

    line1 = input_data[0].split()
    b_date_str, b_tz_str = line1[0], line1[1]
    b_y, b_m, b_d = map(int, b_date_str.split('-'))
    b_offset = parse_tz(b_tz_str)

    line2 = input_data[1].split()
    c_date_str, c_tz_str = line2[0], line2[1]
    c_y = int(c_date_str.split('-')[0])
    c_offset = parse_tz(c_tz_str)

    current_utc = get_utc_time(c_date_str, c_offset)

    target_year = c_y
    b_utc = get_birthday_utc(target_year, b_m, b_d, b_offset)

    if b_utc < current_utc:
        target_year += 1
        b_utc = get_birthday_utc(target_year, b_m, b_d, b_offset)

    delta_s = (b_utc - current_utc).total_seconds()

    if delta_s <= 0:
        print(0)
    else:
        print(math.ceil(delta_s / 86400))

if __name__ == '__main__':
    solve()