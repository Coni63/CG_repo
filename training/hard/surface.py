import sys
import math

def explore_lake(ID, start_x, start_y):
    queue = [(start_x, start_y)]
    surface = 0
    while len(queue) > 0:
        x, y = queue.pop(0)
        carte[y][x] = ID
        surface += 1
        if carte[y+1][x] == "O":
            carte[y+1][x] = "?"  # pour eviter de vérifier que ce ne sois pas dans la queue
            queue.append((x, y+1))
        if carte[y-1][x] == "O":
            carte[y-1][x] = "?"
            queue.append((x, y-1))
        if carte[y][x+1] == "O":
            carte[y][x+1] = "?"
            queue.append((x+1, y))
        if carte[y][x-1] == "O": 
            carte[y][x-1] = "?"
            queue.append((x-1, y))
    lake[ID] = surface
    return surface

l = int(input())
h = int(input())

carte = [["#"]*(l+2)]
for i in range(h):
    row = ["#"]+list(input())+["#"]
    carte.append(row)
carte += [["#"]*(l+2)]

lake = {}
idx = 1
n = int(input())
for i in range(n):
    x, y = [int(j) for j in input().split()]
    x += 1
    y += 1
    if carte[y][x] == "#":
        print(0)
    elif carte[y][x] == "O":
        print(explore_lake(idx, x, y))
        idx += 1
    else:
        print(lake[carte[y][x]])
