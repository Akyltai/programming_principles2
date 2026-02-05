import sys

data = sys.stdin.read().split()
data = data[1:]
first = {}

for index,s in enumerate(data,1):
    if s not in first:
        first[s] = index

sorting = sorted(first.keys())
for i in sorting:
    print(f"{i} {first[i]}")