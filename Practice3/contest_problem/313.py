def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
data = list(map(int, input().split()))

primes = list(filter(lambda x: is_prime(x), data))

if len(primes) > 0:
    print(*(primes))
else:
    print("No primes")