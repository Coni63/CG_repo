import sys
import math
import itertools

def clumps(nums, base):
    c=0
    for a, b in itertools.groupby(nums, key=lambda x:x%base):
        c+=1
    return c

n = [int(x) for x in input()]


m = 0
flag=True
res = "Normal"
for d in range(1, 10):
    k = clumps(n, d)
    if k >= m:
        m = k
    else:
        flag = False
        res = d
        break
print(res)
