import sys
import math
import numpy as np

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
arr = []
n = int(input())
for i in range(n):
    x, y = [int(j) for j in input().split()]
    arr.append([x, y])

arr = np.array(arr, dtype = np.int32)
print(arr, file=sys.stderr)
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print("answer")
