n = int(input())
nums = map(int,list(input().split()))
res = sum(map(lambda x: x*x,nums))
print(res)