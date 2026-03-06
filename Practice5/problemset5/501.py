import re

txt = input()
x = re.match(r"Hello",txt)
if x:
    print("Yes")
else:
    print("No")