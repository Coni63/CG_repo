import sys
import math


s_x, s_y = 0, 0
e_x, e_y = 0, 0

block = []

w, h = [int(i) for i in input().split()]
for i in range(h):
    row = input()
    if "B" in row:
        s_y = i
        s_x = row.index("B")
    if "E" in row:
        e_y = i
        e_x = row.index("E")
    if "#" in row:
        for j in range(w):
            if row[j] == "#":
                block.append((j, i))
        
print(s_x, s_y,file=sys.stderr)
print(e_x, e_y,file=sys.stderr)

target = (e_x, e_y)

moves = [
    (2, -1), 
    (2, 1), 
    (-2, 1), 
    (-2, -1), 
    (1, 2), 
    (1, -2), 
    (-1, 2), 
    (-1, -2)
]

visited = []
nb_move = [0]
queue = [(s_x, s_y)]
result = -1
while len(queue)>0:
    p_x, p_y = queue.pop(0)                   # position a changer
    move = nb_move.pop(0)
    visited.append((p_x, p_y))
    if move < 14 and result == -1:
        for m_x, m_y in moves:                    # move à faire
            n_x, n_y =  p_x+m_x, p_y+m_y          # next position
            pos = (n_x, n_y)
            if pos == target:
                result = move+1
            else:
                if 0<=n_x<w and 0<=n_y<h:
                    if pos not in visited:
                        if pos not in block:
                            queue.append(pos)
                            nb_move.append(move+1)
    else:
        break
            
if result == -1 :
    print("Impossible")
else:
    print(result)

