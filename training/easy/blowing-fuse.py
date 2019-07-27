import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
maxi = 0
fuse = True
n, m, c = [int(i) for i in input().split()]
conso = [int(i) for i in input().split()]
active = [0] * n

for i in input().split():
    mx = int(i)
    active[mx-1] = conso[mx-1] - active[mx-1]  # - active to have the swithc On/Off
    maxi = max(maxi, sum(active))
    if sum(active) > c:
        fuse = False
        break

if not fuse:  
    print("Fuse was blown.")
else:
    print("Fuse was not blown.")
    print("Maximal consumed current was {} A.".format(maxi))
