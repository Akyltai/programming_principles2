import re
n = input()
patt = r'^\d+$'
patt = re.compile(pattern=patt)
s = re.search(patt, n)
if s: print("Match")
else: print("No match")