import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

reverse = {"normal":"reversed", "reversed":"normal"}

grid = []
grad = []

inertia = int(input())

w, h = [int(i) for i in input().split()]
for i in range(h):
    row = input()
    grid.append(row)
    print(row, file=sys.stderr)

for x in range(w):
    for y in range(h):
        if grid[y][x] == "_": 
            grad.append(0)
            break
        if grid[y][x] == ("\ ").rstrip(): #rstrip car "\" ne marche pas ...
            grad.append(-1)
            break
        if grid[y][x] == "/":
            grad.append(1)
            break

#print(grad, file=sys.stderr)

pos = 0
direction = "normal"

while True:
    print(pos, inertia, direction, file=sys.stderr)
    if grad[pos] == 0:
        inertia -= 1
    elif (grad[pos] == -1 and direction == "normal") or (grad[pos] == 1 and direction == "reversed"):
        inertia += 9
    elif (grad[pos] == 1 and direction == "normal") or (grad[pos] == -1 and direction == "reversed"):
        inertia -= 10
    
    if direction == "normal" and pos == w-1:
        print(w-1)
        break

    if direction == "reversed" and pos == 0:
        print(0)
        break

    if inertia > 0:
        if direction == "normal":
            pos +=1
        else:
            pos -=1
    elif inertia == 0:
        if grad[pos] == 0:
            print(pos)
            break
        elif (grad[pos] == 1 and direction == "normal") or (grad[pos] == -1 and direction == "reversed"):
            direction = reverse[direction]
            inertia = 9
            if direction == "normal":
                pos +=1
            else:
                pos -=1
    else:
        direction = reverse[direction]
        inertia = abs(inertia)


# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

