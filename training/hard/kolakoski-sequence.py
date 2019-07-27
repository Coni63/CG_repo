import sys
import math
from itertools import cycle

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
a, b = [int(i) for i in input().split()]

generator = cycle([a, b])

if a == 1:
    l = [a]*a+[b]*b
    i = 2
else:
    l = [a]*a
    i = 1
    next(generator)

while len(l) < n:
    l+=[next(generator)] * l[i]
    i+=1

print("".join(map(str, l[:n])))