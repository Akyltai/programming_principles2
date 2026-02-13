import sys

def solve():
    n = int(input())
    

    arr = list(map(int, input().split()))
    
    q = int(input())
    for _ in range(q):
        command = input().split()
        op = command[0]
        
        if op == 'add':
            x = int(command[1])
            arr = list(map(lambda a: a + x, arr))
            
        elif op == 'multiply':
            x = int(command[1])
            arr = list(map(lambda a: a * x, arr))
            
        elif op == 'power':
            x = int(command[1])
            arr = list(map(lambda a: a ** x, arr))
            
        elif op == 'abs':
            arr = list(map(lambda a: abs(a), arr))
    print(*(arr))

solve()