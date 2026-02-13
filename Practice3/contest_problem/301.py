import sys

data = sys.stdin.read().split()
for j in data:
    for i in j:
        i = int(i)
        if i%2 != 0:
            print("Not valid")    
            break
    else:
        print("Valid")