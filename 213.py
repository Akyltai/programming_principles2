n = int(input(":"))
is_prime = True
j = 1
for i in range(n):
    j+=1
    if n%(j*j) == 0:
        is_prime = True
if is_prime:
    print("YES")
else:
    print("NO")