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
    row, col = pos
    if direction == "^":
        if row == 0:
            return "#"
        else:
            return grid[row-1][col]
    elif direction == "<":
        if col == 0:
            return "#"
        else:
            return grid[row][col-1]
    elif direction == "v":
        if row == height-1:
            return "#"
        else:
            return grid[row+1][col]
    elif direction == ">":
        if col == width-1:
            return "#"
        else:
            return grid[row][col+1]
            
def move(pos, direction):
    row, col = pos
    if direction == "^":
        return (row-1, col)
    elif direction == "<":
        return (row, col-1)
    elif direction == "v":
        return (row+1, col)
    elif direction == ">":
        return (row, col+1)

width, height = [int(i) for i in input().split()]

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
    count.append([0 if x=="0" else x for x in row])
side = input()

print(starting_point, direction, file=sys.stderr)
print(count, file=sys.stderr)

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
    
    if current_pos == starting_point:
        break

print(count, file=sys.stderr)

for row in count:
    print(*row, sep="")
