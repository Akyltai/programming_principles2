import sys

data = sys.stdin.read().split()

numbers = data[1:]

seen = set()

for x in numbers:
    if x in seen:
        print("NO")
    else:
        print("YES")
        seen.add(x)