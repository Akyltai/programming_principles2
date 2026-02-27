import json

def diff(a, b, path=""):
    keys = sorted(set(a.keys()) | set(b.keys()))
    
    for k in keys:
        p = f"{path}.{k}" if path else k
        
        in_a = k in a
        in_b = k in b
        if in_a and in_b and isinstance(a[k], dict) and isinstance(b[k], dict):
            diff(a[k], b[k], p)
        elif not in_a or not in_b or a[k] != b[k]:
            v1 = json.dumps(a[k], separators=(',',':')) if in_a else "<missing>"
            v2 = json.dumps(b[k], separators=(',',':')) if in_b else "<missing>"
            
            print(f"{p} : {v1} -> {v2}")

def main():
    try:
        obj1_str = input()
        obj2_str = input()
        
        obj1 = json.loads(obj1_str)
        obj2 = json.loads(obj2_str)
        if obj1 == obj2:
            print("No differences")
        else:
            diff(obj1, obj2)
            
    except EOFError:
        pass

if __name__ == '__main__':
    main()