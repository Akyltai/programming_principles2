import sys

data = sys.stdin.read().splitlines()
data = data[1:]

MONGO_DB = {}

for line in data:
    parts = line.split()
    cmd = parts[0]
    key = parts[1]

    if cmd == 'set':
        value = parts[2]
        MONGO_DB[key] = value

    elif cmd == 'get':
        if key in MONGO_DB:
            print(MONGO_DB[key])
        else:
            print(f"KE: no key {key} found in the document")