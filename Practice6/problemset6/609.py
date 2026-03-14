n = input()
dct = {}
lets = list(input().split(' '))
nums = list(input().split(' '))
key = input()
try:
    for item in zip(nums,lets):
        dct[item[1]] = item[0]
    print(dct[key])
except KeyError:
    print("Not found")