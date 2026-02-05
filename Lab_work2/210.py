n = int(input())
lst = list(map(int,input().split()))

sort_lst = sorted(lst,reverse=True)
print(*(sort_lst))