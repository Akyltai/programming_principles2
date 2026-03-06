import re

txt = input()

ptr = r'\b[a-zA-Z]{3}\b'

print(len(re.findall(ptr,txt)))