import re

txt = input()
ptr = r'cat|dog'
if re.search(ptr,txt):
    print("Yes")
else:
    print("No")