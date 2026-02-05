import sys
from collections import Counter


data = list(map(int, sys.stdin.read().split()))[1:]
counts = Counter(data)
result = min(counts.keys(), key=lambda x: (-counts[x], x))
print(result)