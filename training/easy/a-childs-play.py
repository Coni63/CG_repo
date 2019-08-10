import sys
import math

class State:
    def __init__(self, pos, k , direction):
        self.pos = pos
        self.k = k
        self.direction = direction
        
    def __hash__(self):
        row, col = self.pos
        p = row*w + col
        q = 1000 * ["U", "L", "D", "R"].index(self.direction) # h*w < 200
        return p + q
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def look(pos, direction):
    row, col = pos
    if direction == "U":
        if row == 0:
            return "#"
        else:
            return grid[row-1][col]
    elif direction == "L":
        if col == 0:
            return "#"
        else:
            return grid[row][col-1]
    elif direction == "D":
        if row == h-1:
            return "#"
        else:
            return grid[row+1][col]
    elif direction == "R":
        if col == w-1:
            return "#"
        else:
            return grid[row][col+1]

def move(pos, direction):
    row, col = pos
    if direction == "U":
        return (row-1, col)
    elif direction == "L":
        return (row, col-1)
    elif direction == "D":
        return (row+1, col)
    elif direction == "R":
        return (row, col+1)

rotate = {
    "U" : "R",
    "R" : "D",
    "D" : "L",
    "L" : "U",
}

history = {}

w, h = [int(i) for i in input().split()]
grid = []
direction = "U"

n = int(input())
for i in range(h):
    line = list(input())
    grid.append(line)
    if "O" in line:
        pos = (i, line.index("O"))

k = 0
while k < n:
    state = State(pos, k, direction)
    h = hash(state)
    if h in history:
        loop_size = k - history[h].k
        # print(k, loop_size, file=sys.stderr)
        remaining = n-k
        n = k + remaining % loop_size
        
    for _ in range(4): # 4 directions
        brick = look(pos, direction)
        if brick == "#":
            direction = rotate[direction]
    
    history[h] = state
    pos = move(pos, direction)
    k+=1
    
print(pos[1], pos[0])
