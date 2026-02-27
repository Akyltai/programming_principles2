def divisibility_gen(n):
    for i in range(0,n+1,12):
        yield(i)
n = int(input())
div = divisibility_gen(n)

fisrt = True
for num in div:
    if not fisrt:
        print(" ",end="")
    print(num,end="")
    fisrt = False
print()