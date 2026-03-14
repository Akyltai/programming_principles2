n = input()
nums = list(map(int,list(input().split(' '))))
if all(num >= 0 for num in nums):
    print("Yes")
else:
    print("No")