import re
n = input()
s = re.findall(r"[0-9]{2,}", n)
for i in s: print(i, end=" ")