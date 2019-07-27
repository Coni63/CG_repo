import sys
import math
import numpy as np
from collections import defaultdict
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

w, h = [int(i) for i in input().split()]
m = []
for i in range(h):
    row = input()
    m.append([1 if x=="#" else 0 for x in row])

m=np.array(m)
split = (m.sum(axis=0) == 0)

result = defaultdict(list)
s=-1
e=0
max_h_temp = 0
trigger = True
for i in range(w):
    if split[i]: 
        if max_h_temp > 0:
            e = i-1
            result[max_h_temp].append((s,e))
        e = 0
        max_h_temp = 0
        s = -1
    if not split[i]:
        if s == -1:
            s = i
        max_h_temp = max(m.sum(axis=0)[i], max_h_temp)

if max_h_temp > 0:
    e = w-1
    result[max_h_temp].append((s,e))

print(result, file=sys.stderr)    
print(m, file=sys.stderr)

max_h = max(result.keys())
building_index = result[max_h]

first = True
for x, y in building_index:
    if first:
        first = False
    else:
        print("")
        
    building = m[:, x:y+1]
    for line in building:
        if sum(line) > 0:
            print("".join(["#" if x == 1 else " " for x in line]).rstrip())
    
