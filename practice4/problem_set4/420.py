import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    num_commands = int(input_data[0])
    g = 0
    n = 0
    
    idx = 1
    for _ in range(num_commands):
        if idx >= len(input_data):
            break
        scope = input_data[idx]
        val = int(input_data[idx+1])
        
        if scope == "global":
            g += val
        elif scope == "nonlocal":
            n += val
            
        idx += 2
        
    print(f"{g} {n}")

if __name__ == '__main__':
    solve()