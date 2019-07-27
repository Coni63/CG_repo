import sys
import math
import statistics

p_x = []
p_y = []
n = int(input())
for i in range(n):
    x, y = [int(j) for j in input().split()]
    p_x.append(x)
    p_y.append(y)
    
lx = max(p_x)-min(p_x)
med = int(statistics.median(p_y))
ly = sum([abs(y-med) for y in p_y])
print(lx + ly)