import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())

if n == 1:
    res = 1
else:
    res = n**3 - (n-2)**3
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print(res)
