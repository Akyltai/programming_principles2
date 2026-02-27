def gen_power_of_two(n):
    a = 0
    while a<=n:
        yield 2**a
        a+=1
n = int(input())
gen = gen_power_of_two(n)
for x in gen:
    print(x,end=" ")