import sys
import math
import time
# import numpy as np

def distanceClosestUnknown(row, col):
    q = [(row, col, [])]
    explored = set()
    while True:
        # print(*q, sep="\n", file=sys.stderr)
        y, x, path = q.pop(0)
        x = x%width
        y = y%height
    
        left_row = y
        left_col = (x-1+width)%width
        if (left_row, left_col) in explored:
            pass
        elif grid[left_row][left_col] == "_" and not visited[left_row][left_col]:
            path2 = path[:]
            path2.append("LEFT")
            return path2
        elif grid[left_row][left_col] == "_" and visited[left_row][left_col]:
            path2 = path[:]
            path2.append("LEFT")
            q.append((left_row, left_col, path2))
        
        up_row = (y-1+height)%height
        up_col = x
        if (up_row, up_col) in explored:
            pass
        elif grid[up_row][up_col] == "_" and not visited[up_row][up_col]:
            path2 = path[:]
            path2.append("UP")
            return path2
        elif grid[up_row][up_col] == "_" and visited[up_row][up_col]:
            path2 = path[:]
            path2.append("UP")
            q.append((up_row, up_col, path2))
        
        right_row = y
        right_col =(x+1)%width
        if (right_row, right_col) in explored:
            pass
        elif grid[right_row][right_col] == "_" and not visited[right_row][right_col]:
            path2 = path[:]
            path2.append("RIGHT")
            return path2
        elif grid[right_row][right_col] == "_" and visited[right_row][right_col]:
            path2 = path[:]
            path2.append("RIGHT")
            q.append((right_row, right_col, path2))
        
        down_row = (y+1)%height
        down_col = x
        if (down_row, down_col) in explored:
            pass
        elif grid[down_row][down_col] == "_" and not visited[down_row][down_col]:
            path2 = path[:]
            path2.append("DOWN")
            return path2
        elif grid[down_row][down_col] == "_" and visited[down_row][down_col]:
            path2 = path[:]
            path2.append("DOWN")
            q.append((down_row, down_col, path2))
        explored.add((y, x))
            
def distanceBetween(row_me, col_me, row_other, col_other):
    """ Manhattan distance with border connected"""
    dx = col_me - col_other
    dx = min(abs(dx), abs(width - dx))
    dy = row_me - row_other
    dy = min(abs(dy), abs(height - dy))
    return dx + dy

def show():
    """
    Render the grid
    """
    for row in range(height):
        for col in range(width): 
            if (row, col) in ennemis:
                print("+", end='', file=sys.stderr)
            elif (row, col) == (y, x):
                print("@", end='', file=sys.stderr)
            elif visited[row][col]:
                print(" ", end='', file=sys.stderr)
            elif grid[row][col] == "_":
                print(".", end='', file=sys.stderr)
            else:
                print(grid[row][col], end='', file=sys.stderr)
        print(file=sys.stderr)

def getPossibleMove():
    possible_move = []
    if left == "_": 
        d_min = 1e6
        next_row = y
        next_col = (x-1+width)%width
        for ennemy in ennemis:
            d = distanceBetween(next_row, next_col, ennemy[0], ennemy[1])
            d_min = min(d_min, d)
        possible_move.append(("LEFT", d_min, (next_row, next_col)))
    if up == "_":
        d_min = 1e6
        next_row = (y-1+height)%height
        next_col = x
        for ennemy in ennemis:
            d = distanceBetween(next_row, next_col, ennemy[0], ennemy[1])
            d_min = min(d_min, d)
        possible_move.append(("UP", d_min, (next_row, next_col)))
    if right == "_":
        d_min = 1e6
        next_row = y
        next_col =(x+1)%width
        for ennemy in ennemis:
            d = distanceBetween(next_row, next_col, ennemy[0], ennemy[1])
            d_min = min(d_min, d)
        possible_move.append(("RIGHT", d_min, (next_row, next_col)))
    if down == "_": 
        d_min = 1e6
        next_row = (y+1)%height
        next_col = x
        for ennemy in ennemis:
            d = distanceBetween(next_row, next_col, ennemy[0], ennemy[1])
            d_min = min(d_min, d)
        possible_move.append(("DOWN", d_min, (next_row, next_col)))
    return possible_move


direction = {'UP' : 'C', 'RIGHT' : 'A', 'DOWN' : 'D', 'LEFT' : 'E', 'STAY' : 'B'}
invert = {'UP' : 'DOWN', 'RIGHT' : 'LEFT', 'DOWN' : 'UP', 'LEFT' : 'RIGHT', 'STAY' : 'STAY'}

width = int(input())
height = int(input())
players = int(input())

print(f"{height} x {width}", file=sys.stderr)

grid = [['?' for x in range(width)] for y in range(height)]
visited = [[False for x in range(width)] for y in range(height)]

previous_move = None
# game loop
while True:
    up = input()
    right = input()
    down = input()
    left = input()
    
    ennemis = []
    
    for i in range(players-1):
        x, y = [int(j) for j in input().split()]
        x = x%width
        y = y%height
        ennemis.append((y, x))
        grid[y][x] = "_"
    
    x, y = [int(j) for j in input().split()]
    x = x%width
    y = y%height
    visited[y][x] = True
    print(x, y, file=sys.stderr)
    
    tic = time.time()
    
    grid[(y-1+height)%height][x] = up
    grid[(y+1)%height][x] = down
    grid[y][(x+1)%width] = right
    grid[y][(x-1+width)%width] = left
    
    possible_move = getPossibleMove()
    
    if len(possible_move) == 0:
        print(direction["WAIT"])  
    elif len(possible_move) == 1:
        move, next_d, next_pos = possible_move[0]
        print(direction[move])
        previous_move = move
    else:
        sorted_possibilities = sorted(possible_move, key = lambda x : x[1], reverse=True)
        if sorted_possibilities[0][1] < 3:
            move, next_d, next_pos = sorted_possibilities[0]
            print(direction[move])
            previous_move = move
        else:
            path = distanceClosestUnknown(y, x)
            move = path[0]
            print(direction[move])
            print(path, file=sys.stderr)
            previous_move = move
            # done = False
            # for move, next_d, next_pos in sorted_possibilities:
            #     next_row, next_col = next_pos
            #     if not visited[next_row][next_col]:
            #         print(direction[move])
            #         previous_move = move
            #         done = True
            #         break
            # if not done:
            #     for move, next_d, next_pos in sorted_possibilities:
            #         if previous_move != invert[move]:
            #             print(direction[move])
            #             previous_move = move
            #             break

    show()

    toc = time.time()
        
    score = 2*sum([sum(x) for x in visited])
    
    print(score, toc - tic, file=sys.stderr)
