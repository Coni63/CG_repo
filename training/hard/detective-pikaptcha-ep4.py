import sys
import math

import sys
import math


inverte = {"R" : "L", "L" : "R"}

rotate = {
    "R" : {
        "^" : ">", 
        ">" : "v", 
        "v" : "<", 
        "<" : "^"
        },   
    "L" : {
        "^" : "<", 
        "<" : "v",
        "v" : ">", 
        ">" : "^"
        }   
}

def look(pos, direction):
    front_face, front_row, front_col, new_dir = move(pos, direction)
    return grid[front_face][front_row][front_col]
            
def move(pos, direction):
    face, row, col = pos
    if face == 1:
        if direction == "^":
            if row == 0:
                return 6, n-1, col, "^"
            else:
                return face, row-1, col, direction
        elif direction == "<":
            if col == 0:
                return 2, 0, row, "v"
            else:
                return face, row, col-1, direction
        elif direction == "v":
            if row == n-1:
                return 3, 0, col, "v"
            else:
                return face, row+1, col, direction
        elif direction == ">":
            if col == n-1:
                return 4, 0, n-row-1, "v"
            else:
                return face, row, col+1, direction
    if face == 2:
        if direction == "^":
            if row == 0:
                return 1, col, 0, ">"
            else:
                return face, row-1, col, direction
        elif direction == "<":
            if col == 0:
                return 6, n-row-1, 0, ">"
            else:
                return face, row, col-1, direction
        elif direction == "v":
            if row == n-1:
                return 5, n-col-1, 0, ">"
            else:
                return face, row+1, col, direction
        elif direction == ">":
            if col == n-1:
                return 3, row, 0, ">"
            else:
                return face, row, col+1, direction
    if face == 3:
        if direction == "^":
            if row == 0:
                return 1, n-1, col, "^"
            else:
                return face, row-1, col, direction
        elif direction == "<":
            if col == 0:
                return 2, row, n-1, "<"
            else:
                return face, row, col-1, direction
        elif direction == "v":
            if row == n-1:
                return 5, 0, col, "v"
            else:
                return face, row+1, col, direction
        elif direction == ">":
            if col == n-1:
                return 4, row, 0, ">"
            else:
                return face, row, col+1, direction
    if face == 4:
        if direction == "^":
            if row == 0:
                return 1, n-col-1, n-1, "<"
            else:
                return face, row-1, col, direction
        elif direction == "<":
            if col == 0:
                return 3, row, n-1, "<"
            else:
                return face, row, col-1, direction
        elif direction == "v":
            if row == n-1:
                return 5, col, n-1, "<"
            else:
                return face, row+1, col, direction
        elif direction == ">":
            if col == n-1:
                return 6, n-row-1, n-1, "<"
            else:
                return face, row, col+1, direction
    if face == 5:
        if direction == "^":
            if row == 0:
                return 3, n-1, col, "^"
            else:
                return face, row-1, col, direction
        elif direction == "<":
            if col == 0:
                return 2, n-1, n-row-1, "^"
            else:
                return face, row, col-1, direction
        elif direction == "v":
            if row == n-1:
                return 6, 0, col, "v"
            else:
                return face, row+1, col, direction
        elif direction == ">":
            if col == n-1:
                return 4, n-1, row, "^"
            else:
                return face, row, col+1, direction
    if face == 6:
        if direction == "^":
            if row == 0:
                return 5, n-1, col, "^"
            else:
                return face, row-1, col, direction
        elif direction == "<":
            if col == 0:
                return 2, n-row-1, 0, ">"
            else:
                return face, row, col-1, direction
        elif direction == "v":
            if row == n-1:
                return 1, 0, col, "v"
            else:
                return face, row+1, col, direction
        elif direction == ">":
            if col == n-1:
                return 4, n-row-1, n-1, "<"
            else:
                return face, row, col+1, direction

grid = [[]]  # index 0 has empty list to have same number as the drawing
count = [[]]
n = int(input())
for i in range(1, 7):
    subgrid = []
    subcount = []
    for j in range(n):
        row = list(input())
        intersect = set(row).intersection({"^", ">", "v", "<"})
        if len(intersect) > 0:
            direction = intersect.pop()
            col = row.index(direction)
            starting_point = (i, j, col)
            row[col] = "0"
        subgrid.append(row)
        subcount.append([0 if x=="0" else x for x in row])
    grid.append(subgrid)
    count.append(subcount)
    
side = input()

for i in range(n):
    print(" "*n + "".join(grid[1][i]), file=sys.stderr)
for i in range(n):
    print("".join(grid[2][i]) +
          "".join(grid[3][i]) + 
          "".join(grid[4][i]), file=sys.stderr)
for i in range(n):
    print(" "*n + "".join(grid[5][i]), file=sys.stderr)
for i in range(n):
    print(" "*n + "".join(grid[6][i]), file=sys.stderr)
    
print(starting_point, direction, side, file=sys.stderr)
# print(count, file=sys.stderr)

current_pos = starting_point
while True:
    direction = rotate[side][direction]
    valid = False
    for _ in range(4): # 4 directions
        brick = look(current_pos, direction)
        if brick == "#":
            direction = rotate[inverte[side]][direction]
        else:
            valid = True
    
    if not valid:
        break
    
    *current_pos, direction = move(current_pos, direction)
    print(current_pos, file=sys.stderr)
    count[current_pos[0]][current_pos[1]][current_pos[2]] += 1
    
    # print(current_pos, starting_point, direction, file=sys.stderr)
    
    if tuple(current_pos) == starting_point:
        break


for subgrid in count:
    for row in subgrid:
        print(*row, sep="")
