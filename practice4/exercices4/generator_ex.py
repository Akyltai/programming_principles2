#1
def sqr_gen(n):
    for i in range(n+1):
        yield i*i
gen_s = sqr_gen(int(input()))
for i in gen_s:
    print(i)
#2
def even_gen(n):
    for i in range(n+1):
        if i%2 == 0:
            yield i
gen_e = even_gen(int(input()))
for i in gen_e:
    print(i)
#3
def twl_gen(n):
    for i in range(0,n+1,12):
        yield i
gen_t = twl_gen(int(input()))
for i in gen_t:
    print(i)
#4
def squares_gen(a,b):
    for i in range(a,b+1):
        yield i*i
gen_sq = squares_gen(int(input()),int(input()))
for i in gen_sq:
    print(i)
#5
def zer_gen(n):
    while n>=0:
        yield n
        n-=1
gen_z = zer_gen(int(input()))
for i in gen_z:
    print(i)