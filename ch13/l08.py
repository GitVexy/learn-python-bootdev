from functools import reduce
def cool_join_strings(strings):
    if not strings:
        return ""
    return reduce(lambda x, y : print(x, y), strings)
    
def join_strings(strings):
    if not strings:
        return ""
    
    out = ""
    for s in strings:
       out += s + ","
    return out[:-1]

print(join_strings([]))