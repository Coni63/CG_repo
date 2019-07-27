import sys
import math
import numpy as np

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

width, height = [int(i) for i in input().split()]
count = int(input())
mat = []
for i in range(height):
    raster = input()
    raster = sorted(raster, key=lambda x: ord(x), reverse = True)
    mat.append(raster)

if count % 2 == 1:
    mat = np.array(mat).T
else:
    mat = np.array(mat)
    
for line in mat:
    print("".join(line))
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)


