import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())

table = [int(input()) for i in range(n)]
table.sort()

diff = [table[i+1]-table[i] for i in range(n-1)]

print(min(diff))
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)


