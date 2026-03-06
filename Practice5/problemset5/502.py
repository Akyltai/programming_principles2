import re

strg = input()
sbt = input()

x = re.search(sbt,strg)
if x:
    print("Yes")
else:
    print("No")