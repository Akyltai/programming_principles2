import re

txt = input()
a = input()

lst = (re.split(a,txt))
print(','.join(lst))