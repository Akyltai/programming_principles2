import sys
from datetime import datetime, timedelta

def parse_datetime(line):
    parts = line.strip().split()
    date_str, time_str, tz_str = parts[0], parts[1], parts[2]
    
    y, m, d = map(int, date_str.split('-'))
    H, M, S = map(int, time_str.split(':'))
    
    sign = 1 if '+' in tz_str else -1
    tz_parts = tz_str.replace('UTC+', '').replace('UTC-', '').split(':')
    tz_offset_minutes = sign * (int(tz_parts[0]) * 60 + int(tz_parts[1]))
    
    local_dt = datetime(y, m, d, H, M, S)
    return local_dt - timedelta(minutes=tz_offset_minutes)

def solve():
    input_data = sys.stdin.read().splitlines()
    if len(input_data) < 2:
        return
        
    start_utc = parse_datetime(input_data[0])
    end_utc = parse_datetime(input_data[1])
    
    diff = int((end_utc - start_utc).total_seconds())
    print(diff)

if __name__ == '__main__':
    solve()