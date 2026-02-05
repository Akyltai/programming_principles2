n = int(input())
lst = list(map(int,input().split()))
max = -9999999
for i in lst:
    if i>max:
        max = i
print(max)