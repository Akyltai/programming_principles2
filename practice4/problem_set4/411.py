import json
import sys

def apply_patch(source, patch):
    for key, value in patch.items():
        if value is None:
            if key in source:
                del source[key]
        elif isinstance(value, dict) and isinstance(source.get(key), dict):
            apply_patch(source[key], value)
        else:
            source[key] = value
    return source

def main():
    input_data = sys.stdin.read().splitlines()
    
    if len(input_data) >= 2:
        source_obj = json.loads(input_data[0])
        patch_obj = json.loads(input_data[1])
        patched_result = apply_patch(source_obj, patch_obj)
        print(json.dumps(patched_result, separators=(',', ':'), sort_keys=True))

if __name__ == '__main__':
    main()