import json
import sys

def main():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return

    json_str = input_data[0]
    try:
        data = json.loads(json_str)
    except json.JSONDecodeError:
        return

    n = int(input_data[1])

    for i in range(2, 2 + n):
        query = input_data[i].strip()
        if not query:
            continue

        normalized_query = query.replace('[', '.[')
        
        parts = [p for p in normalized_query.split('.') if p]

        current = data
        found = True

        for part in parts:
            if part.startswith('[') and part.endswith(']'):
                idx_str = part[1:-1]
                
                if idx_str.isdigit() and isinstance(current, list):
                    idx = int(idx_str)
                    if 0 <= idx < len(current):
                        current = current[idx]
                    else:
                        found = False
                        break
                else:
                    found = False
                    break
            
            else:
                if isinstance(current, dict) and part in current:
                    current = current[part]
                else:
                    found = False
                    break

        if found:
            print(json.dumps(current, separators=(',', ':')))
        else:
            print("NOT_FOUND")

if __name__ == '__main__':
    main()