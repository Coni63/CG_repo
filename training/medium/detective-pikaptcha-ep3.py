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
    front_row, front_col = move(pos, direction)
    return grid[front_row][front_col]
            
def move(pos, direction):
    row, col = pos
    if direction == "^":
        if row == 0:
            return height-1, (width//2+col)%width
        else:
            return row-1, col
    elif direction == "<":
        if col == 0:
            return row, width-1
        else:
            return row, col-1
    elif direction == "v":
        if row == height-1:
            return 0, (width//2+col)%width
        else:
            return row+1, col
    elif direction == ">":
        if col == width-1:
            return row, 0
        else:
            return row, col+1
        

width, height = [int(i) for i in input().split()]
print(width, height, file=sys.stderr)

grid = []
count = []
for i in range(height):
    row = list(input())
    intersect = set(row).intersection({"^", ">", "v", "<"})
    if len(intersect) > 0:
        direction = intersect.pop()
        col = row.index(direction)
        starting_point = (i, col)
        row[col] = "0"
    grid.append(row)
    print("".join(row), file=sys.stderr)
    count.append([0 if x=="0" else x for x in row])
    
side = input()

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
    
    current_pos = move(current_pos, direction)
    count[current_pos[0]][current_pos[1]] += 1
    
    # print(current_pos, direction, file=sys.stderr)
    
    if current_pos == starting_point:
        break

# print(count, file=sys.stderr)

for row in count:
    print(*row, sep="")
