z = input()
a = map(int,list(input().split(" ")))
b = map(int,list(input().split(" ")))
sum = 0
for item in zip(a,b):
    sum += item[0]*item[1]
print(sum)