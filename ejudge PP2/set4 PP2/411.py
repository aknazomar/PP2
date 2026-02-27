import json

source = json.loads(input())
patch_obj = json.loads(input())

def apply(source, patch):
    for key, val in patch.items(): 
        if val is None:
        #{"a":5,"b":3}
        #{"a":None}
            source.pop(key, None)
            #{"b":3}
        elif key not in source:
        #{"a":4}
        #{"b":5}
            source[key] = val
            #{"a":4,"b":5}
        elif isinstance(val, dict) and isinstance(source.get(key), dict):
        # {"a":{"x":5,"y":1}}
        # {"a":{"x":None,"z":3,"y":5}}
            apply(source[key], val)
        else:
        #{"a":5}
        #{"a":7}
            source[key] = val
            #{"a":7}

apply(source, patch_obj)

print(json.dumps(source, separators=(',', ":"), sort_keys=True))