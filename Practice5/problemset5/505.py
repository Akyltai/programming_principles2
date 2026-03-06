import re

txt = input()
x = re.compile(txt,'a-z1-0')
y = re.match(x)
print(y)