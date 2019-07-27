import sys
import math

v = eval(input())#[int(x) for x in input()[1:-1].split(",")].sort()
print(v, file=sys.stderr)
v.sort()
print("", file=sys.stderr)

l = len(v)
result = ""
i = 0

while i < len(v):
    for j in range(0, len(v)-i):
        if j == 0:    
            arr = v[i:]
        else:
            arr = v[i:-j]
        
        print(arr, file=sys.stderr)
        
        if ((arr[-1]-arr[0]) == (len(arr)-1)) and (len(arr) > 2):
            #print(i, l-j-1, arr, file=sys.stderr)
            section = arr
            i = l - j - 1
            break
        elif len(arr) == 1:
            section = arr[0]
        
    i += 1
    
    #result.append(section)
    #print(result, file=sys.stderr)
    if isinstance(section, list):
        result += ",%s-%s" % (section[0], section[-1])
    else:
        result += "," + str(section)
            
print(result[1:])
