def gen_count(n):
    while n>=0:
        x = n
        n-=1
        yield x 
n = int(input())
gen = gen_count(n)
for i in gen:
    print(i)