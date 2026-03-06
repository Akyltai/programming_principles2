import re

txt = input()
patt = r'\d{2}/\d{2}/\d{4}'
res = re.findall(patt, txt)
print(len(res))