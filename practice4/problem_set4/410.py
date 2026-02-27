def cyc_gen(lst,n):
    for _ in range(n):
        for i in lst:
            yield i
lst = input().split()
n = int(input())
gen = cyc_gen(lst,n)
for i in gen:
    print(i,end=" ")