import sys
import math
import numpy as np
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

h = int(input())
n = int(input())

grid = []
for i in range(n):
    grid.append([int(j) for j in input().split()])

grid = np.array(grid, np.uint16)
valley = grid <= h
flood_fill = valley.copy()

if flood_fill.sum() == 0:
    print(0)
else:
    valleys = []
    while flood_fill.sum() > 0:
        size = 0
        min_height = 5000
        starting_pts = np.argwhere(flood_fill)[0]
        queue = [starting_pts]
        while len(queue) > 0:
            row, col = queue.pop(0)
            flood_fill[row, col] = False
            size += 1
            min_height = min(min_height, grid[row, col])
            if col > 0 and flood_fill[row, col-1]:
                queue.append((row, col-1))
            if col < n-1 and flood_fill[row, col+1]:
                queue.append((row, col+1))
            if row > 0 and flood_fill[row-1, col]:
                queue.append((row-1, col))
            if row < n-1 and flood_fill[row+1, col]:
                queue.append((row+1, col))
        valleys.append((size, min_height))
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
    valleys.sort(key=lambda x: (-x[0], x[1]))
    print(valleys, file=sys.stderr)
    
    print(valleys[0][1])
