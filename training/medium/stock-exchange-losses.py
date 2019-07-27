import sys
import math

n = int(input())
arr = [int(i) for i in input().split()]

local_min=min(arr[0], arr[1])
local_max=max(arr[0], arr[1])
delta = 0
max_delta = 0

for i in range(2, n):
    if arr[i] < local_max:
        delta = arr[i] - local_max
        if delta < max_delta:
            max_delta = delta
    else:
        local_max = arr[i]    

# To debug: print("Debug messages...", file=sys.stderr)

print(max_delta)
