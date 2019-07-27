import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

maze = []

w, h = [int(i) for i in input().split()]
x_i, y_i = [int(i) for i in input().split()]
for i in range(h):
    r = input()
    maze.append(list(r))
    print(r, file=sys.stderr)
    
out = []
queue = [(y_i, x_i)]
while len(queue) > 0 :
    y, x = queue.pop(0)
    maze[y][x] = "o"
    
    # expand above
    if y >= 1:
        if maze[y-1][x] == ".":
            queue.append((y-1, x))
            if y == 1:
                out.append((x, y-1))
            
    # expand below
    if y < h-1:
        if maze[y+1][x] == ".":
            queue.append((y+1, x))
            if y == h-2:
                out.append((x, y+1))
            
    # expand left
    if x >= 1:
        if maze[y][x-1] == ".":
            queue.append((y, x-1))
            if x == 1:
                out.append((x-1, y))
            
    # expand right
    if x < w-1:
        if maze[y][x+1] == ".":
            queue.append((y, x+1))
            if x == w-2:
                out.append((x+1, y))

for line in maze:
    print("".join(line), file=sys.stderr)

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

out = set(out)
out = sorted(out, key=lambda x:x[0])
print(len(out))
for each in out:
    print(" ".join([str(i) for i in each]))
