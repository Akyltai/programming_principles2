def fibonacci(n):
    a, b = 0, 1
    for f in range(n):
        yield a
        a, b = b, a + b

n = int(input())
print(",".join(str(x) for x in fibonacci(n)))