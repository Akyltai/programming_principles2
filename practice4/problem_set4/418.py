import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    x1 = float(input_data[0])
    y1 = float(input_data[1])
    x2 = float(input_data[2])
    y2 = float(input_data[3])
    
    x = (x1 * y2 + x2 * y1) / (y1 + y2)
    
    print(f"{x:.10f} 0.0000000000")

if __name__ == '__main__':
    solve()