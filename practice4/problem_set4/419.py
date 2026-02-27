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
    
    OA = math.hypot(x1, y1)
    OB = math.hypot(x2, y2)
    
    R = min(R, min(OA, OB))
    
    alpha_A = math.acos(R / OA) if OA > R else 0.0
    alpha_B = math.acos(R / OB) if OB > R else 0.0
    
    theta_A = math.atan2(y1, x1)
    theta_B = math.atan2(y2, x2)
    
    delta_theta = abs(theta_A - theta_B)
    if delta_theta > math.pi:
        delta_theta = 2 * math.pi - delta_theta
        
    if delta_theta > alpha_A + alpha_B + 1e-9:
        arc_angle = delta_theta - alpha_A - alpha_B
        length = math.sqrt(max(0, OA**2 - R**2)) + math.sqrt(max(0, OB**2 - R**2)) + R * arc_angle
        print(f"{length:.10f}")
    else:
        length = math.hypot(x2 - x1, y2 - y1)
        print(f"{length:.10f}")

if __name__ == '__main__':
    solve()