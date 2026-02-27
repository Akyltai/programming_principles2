import sys
import math

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    R = float(input_data[0])
    x1 = float(input_data[1])
    y1 = float(input_data[2])
    x2 = float(input_data[3])
    y2 = float(input_data[4])
    
    dx = x2 - x1
    dy = y2 - y1
    a = dx**2 + dy**2
    
    if a == 0:
        print(f"{0.0:.10f}")
        return
        
    b = 2 * (x1 * dx + y1 * dy)
    c = x1**2 + y1**2 - R**2
    D = b**2 - 4 * a * c
    
    if D < 0:
        print(f"{0.0:.10f}")
        return
        
    sqrt_D = math.sqrt(D)
    t1 = (-b - sqrt_D) / (2 * a)
    t2 = (-b + sqrt_D) / (2 * a)
    
    start_t = max(0.0, min(t1, t2))
    end_t = min(1.0, max(t1, t2))
    
    if start_t < end_t:
        length = (end_t - start_t) * math.sqrt(a)
        print(f"{length:.10f}")
    else:
        print(f"{0.0:.10f}")

if __name__ == '__main__':
    solve()