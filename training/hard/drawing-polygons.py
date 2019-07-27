import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
arr = []
n = int(input())
for i in range(n):
    x, y = [int(j) for j in input().split()]
    arr.append((x, y))
    
first = arr[0]
last = arr[-1]

if last[1] >= first[1]: #si le dernier est plus haut que le 1er
    if last[0] >= first[0] : #si le dernier est a droite
        print("COUNTERCLOCKWISE")
    else:
        print("CLOCKWISE")
else: #si le dernier est moins haut que le 1er
    if last[0] >= first[0] : #si le dernier est a droite
        print("COUNTERCLOCKWISE")
    else:
        print("CLOCKWISE")

    
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
