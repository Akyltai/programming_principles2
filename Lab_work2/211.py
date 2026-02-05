n, l, r = map(int,input().split())
lst = list(map(int,input().split()))
lst[l-1:r] = lst[l-1:r][::-1]
print(*(lst))