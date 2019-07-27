import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())

maxi = 4*n+2

# for mini
sidemax = int(1500000**(1/3))
min_surface = 1e10
for x in range(1, sidemax):
    for y in range(1, sidemax):
        area = x*y
        if n/area == n//area:
            depth = n//area
            surface = y * (2*x + 2*depth) + 2*(x*depth)
            min_surface = min(surface, min_surface)
        
print(depth, file=sys.stderr)

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print(min_surface, maxi)
