import re
user_input = input()
pattern = r'\w+'
pattern = re.compile(pattern=pattern)
s = re.findall(pattern, user_input)
print(len(s))