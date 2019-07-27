import sys
import math
import time

def dfs(k):
    if k == 1:
        return True
    
    res = False
    for v in [2, 3, 5]:
        if k%v == 0:
            res = dfs(k//v)
            if res:
                return res
    return res

n = int(input())

s = time.time()

for i in range(n):
    f = int(input())
    res = dfs(f)
    print("VICTORY" if res else "DEFEAT")
    
print(time.time()-s, file=sys.stderr)
    
