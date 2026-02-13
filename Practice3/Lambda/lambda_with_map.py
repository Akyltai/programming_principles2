import sys
# 1 - power of two
data = list(map(lambda x: int(x)**2,sys.stdin.read().split()))
print(data)
#2 - names capitalize
names = list(map(lambda name: name.capitalize(),sys.stdin.read().split()))
print(names)
#3 - hide email
emails = list(map(lambda email:email[:3]+"***"+email[email.find("@"):],sys.stdin.read().split()))
print(emails)
#4 - current converter
prices = [456,789,101112,23,45,678]
dollars = 494.77
converter = list(map(lambda x:round(int(x)/dollars,2),prices))
print(converter)
#5
data = list(map(int,sys.stdin.read().split()))
for i in data:
    print(type(i))