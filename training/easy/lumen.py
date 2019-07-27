import sys
import math
import numpy as np

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
lamps = []
n = int(input())
l = int(input())
c = 0
for i in range(n):
    line = input().split()
    for j, val in enumerate(line):
        if val == "C":
            lamps.append((c, i, j))
            c += 1

if c == 0:
    print(n*n)
else:
    values = np.zeros(shape=( n, n, c ), dtype=np.int32)
    
    for idx, lamp_x, lamp_y in lamps:
        for i in range(n):
            for j in range(n):
                d = max(abs(j-lamp_y), abs(i-lamp_x))
                values[i, j, idx] = max(0, l-d)
    
    values = values.max(axis=2)
    
    print((values == 0).sum())
