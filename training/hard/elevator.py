import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n, a, b, k, m = [int(i) for i in input().split()]

loop = 0
while True:
    if loop > 10000:
        print("IMPOSSIBLE")
        break
    if k < m: #on doit monter
        k += a
        loop += 1
    elif k > m: #on doit descendre
        k -= b
        loop += 1
    else:
        print(loop)
        break

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

