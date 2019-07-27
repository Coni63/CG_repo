import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
arr = sorted(list(map(int, input().split())))

change = True

while change:
    change = False
    for i in range(len(arr)-1):
        if arr[i+1] == arr[i]:
            value = arr[i]
            arr.pop(i)
            arr.pop(i)
            arr.append(value+1)
            arr.sort()
            change = True
            break
        
    
print(arr, file=sys.stderr)
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print(len(arr))
