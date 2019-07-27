import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

x = int(input())
n = int(input())
bricks = [int(i) for i in input().split()]
bricks.sort(reverse=True)

f = 0
for i, brick in enumerate(bricks):
    L = i//x
    f += L*10*6.5*brick/100 

print("{:.3f}".format(f))
