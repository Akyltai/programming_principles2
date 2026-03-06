import re

txt = input()

dig = re.findall(r'\d',txt)
print(" ".join(dig))