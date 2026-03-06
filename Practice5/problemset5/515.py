import re

n = input()
result = re.sub(r'\d', lambda m: m.group() * 2, n)
print(result)