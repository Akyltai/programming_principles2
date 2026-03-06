import re

strn = input()
nes = input()

x = re.findall(nes,strn)
print(len(x))