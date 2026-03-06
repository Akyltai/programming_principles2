import re

txt = input()
word = input()
rep = input()
x = re.sub(word, rep , txt)
print(x)