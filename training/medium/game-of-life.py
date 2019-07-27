import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

width, height = [int(i) for i in input().split()]

arr = []
out = []

arr.append(["#"] * (width+2))
out.append(["#"] * (width+2))

for _ in range(height):
    arr.append(["#"] + list(input()) + ["#"])
    out.append(["#"]* (width+2))

arr.append(["#"]* (width+2))
out.append(["#"]* (width+2))

for each in arr:
    print(each, file=sys.stderr)

for i in range(1, height + 1):
    print(i, file=sys.stderr)
    for j in range(1, width + 1):
        a = 0
        if arr[i][j-1] == "1": a+=1
        if arr[i][j+1] == "1": a+=1
        if arr[i-1][j+1] == "1": a+=1
        if arr[i-1][j] == "1": a+=1
        if arr[i-1][j-1] == "1": a+=1
        if arr[i+1][j+1] == "1": a+=1
        if arr[i+1][j] == "1": a+=1
        if arr[i+1][j-1] == "1": a+=1
        
        if arr[i][j] == "1":
            if a < 2:
                out[i][j] = "0"
            elif a == 2 or a == 3:
                out[i][j] = "1"
            else:
                out[i][j] = "0"

        if arr[i][j] == "0":
            if a == 3:
                out[i][j] = "1"
            else:
                out[i][j] = "0"

out.pop(0)
out.pop(-1)

for i in range(len(out)):
    out[i] = out[i][1:-1]

for each in out:
    print("".join(each))
    

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

#print("answer")
