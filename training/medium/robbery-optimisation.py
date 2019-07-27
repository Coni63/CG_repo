import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
housevalue = [int(input()) for i in range(n)]
n = len(housevalue)

pn = housevalue[0]
qn = 0
for i in range(1, n):
    pn1 = pn
    qn1 = qn
    pn = qn1 + housevalue[i]
    qn = max(pn1, qn1)
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print(max(pn,qn))
