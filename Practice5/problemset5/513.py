import re
n = input()
s = re.findall("\w+",n)
print(len(s))