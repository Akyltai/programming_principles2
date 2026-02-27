import sys
import importlib

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    idx = 1
    
    for _ in range(n):
        if idx >= len(input_data):
            break
            
        mod_name = input_data[idx]
        attr_name = input_data[idx+1]
        idx += 2
        
        try:
            mod = importlib.import_module(mod_name)
        except ImportError:
            print("MODULE_NOT_FOUND")
            continue
            
        if not hasattr(mod, attr_name):
            print("ATTRIBUTE_NOT_FOUND")
            continue
            
        attr = getattr(mod, attr_name)
        if callable(attr):
            print("CALLABLE")
        else:
            print("VALUE")

if __name__ == '__main__':
    solve()