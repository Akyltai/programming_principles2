import re

txt = input().strip()

ptr = r'\S+@\S+\.\S+'

res = re.search(ptr,txt)
if re.search(ptr,txt):
    print(res[0])
else:
    print("No email")