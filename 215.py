import sys

data = sys.stdin.read().split()
names = data[1:]
unique_names = set(names)
print(len(unique_names))