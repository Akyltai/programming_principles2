def isUsual(num):
    if num <= 0: return False
    for f in (2, 3, 5):
        while num % f == 0:
            num //= f
    return num == 1

n = int(input())
print("Yes" if isUsual(n) else "No")