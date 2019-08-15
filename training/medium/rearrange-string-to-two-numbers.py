import sys
import math

def smallest(lst): 
    if lst == [0]:
        return lst
        
    for i,n in enumerate(lst):  
        if n != 0:  
            tmp = lst.pop(i) 
            break
    return [tmp] + lst

s = [int(x) for x in input()]
s.sort()

print(s, file=sys.stderr)

if sum(s) == 0 and len(s) > 2:
    print(-1, -1)
if sum(s) == 0 and len(s) == 2:
    print(0, 0)
elif sum([x>0 for x in s]) == 1 and s.count(0)>19:
    print(-1, -1)
elif len(s) < 2:
    print(-1, -1)
elif len(s) > 36 and s.count(0) < 2:
    print(-1, -1)
elif len(s) > 38:
    print(-1, -1)
else:
    if s.count(0) >= 18 and s.count(1) >=1 :
        n2 = [1] + [0]*18
        for i in range(18):
            s.pop(0)
        for i, n in enumerate(s):  
            if n == 1:  
                s.pop(i)
                break
        n1 = smallest(s)
    else:
        len_n1 = max(1, len(s)-18)
        len_n2 = len(s)-len_n1
        if len_n1 == 1:
            n1 = [s[0]]
            n2 = smallest(s[1:])
        else:
            tmp = smallest(s)
            n1 = tmp[:len_n1]
            n2 = smallest(tmp[len_n1:])
    n1 = "".join([str(x) for x in n1])
    n2 = "".join([str(x) for x in n2])
    print(n1, n2)
    
