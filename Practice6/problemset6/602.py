n = int(input())
nums = map(int,list(input().split(" ")))
a = filter(lambda x:x%2 == 0,nums)
print(len(list(a)))