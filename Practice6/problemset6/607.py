n = input()
x = []
words = list(input().split(' '))
for i in words:
    x.append(len(i))
for i in words:
    if len(i) == max(x):
        print(i)
        break