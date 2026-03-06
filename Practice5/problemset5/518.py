import re

user_input = input()
nex = input()
escaped_input = re.escape(nex)
s = re.findall(escaped_input, user_input)
print(len(s))