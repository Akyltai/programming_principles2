from datetime import datetime

f =  "%Y-%m-%d UTC%z"
a = input().strip()
b = input().strip()
date_a = datetime.strptime(a,f)
date_b = datetime.strptime(b,f)
diff = abs(date_a - date_b)
days = int(diff.total_seconds()/86400)
print(days)