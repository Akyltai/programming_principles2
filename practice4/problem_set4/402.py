def even_gen(n):
    for i in range(0,n+1,2):
        yield str(i)
n = int(input())
gen = even_gen(n)
print(",".join(gen))