def gen_prime(n):
    for num in range(2,n+1):
        is_prime = True
        for i in range(2,int(num**0.5)+1):
            if num % i == 0:
                is_prime = False
        if is_prime:
            yield num
n = int(input())
gen = gen_prime(n)
for i in gen:
    print(i,end=" ")