n = int(input())
lst = list(map(int,input().split()))
cnt = 0
for i in lst:
    if i>0:
        cnt+=1
print(cnt)