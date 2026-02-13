import sys

data = sys.stdin.read().split()
data = data[1:]

serials = {}

for i in range(0, len(data), 2):
    name = data[i]
    series = int(data[i+1])

    if name in serials:
        serials[name]+= series
    else:
        serials[name] = series

sort = sorted(serials.keys())

for i in sort:
    print (f"{i} {serials[i]}")
    