n = int(input())
lst = list(map(int,input().split()))

mx = max(lst)
mn = min(lst)
for i in range(len(lst)):
    if lst[i] == mx:
        lst[i] = mn
for i in lst:
    print(i,end=" ")