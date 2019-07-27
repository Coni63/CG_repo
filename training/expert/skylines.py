import sys
import math
from itertools import groupby

class tower:
    def __init__(self, H, S, E):
        self.start = S
        self.end = E
        self.height = H
        tower_list.append(self)

    def __repr__(self):
        return "{}=>{} : {}".format(self.start, self.end, self.height)

tower_list = []

n = int(input())
for i in range(n):
    h, x_1, x_2 = [int(j) for j in input().split()]
    tower(h, x_1, x_2)

print(tower_list, file=sys.stderr)

xmin = min(tower_list, key = lambda x:x.start)
xmax = max(tower_list, key = lambda x:x.end)

width = xmax.end - xmin.start
offset = xmin.start

table = [0]*width

for tower in tower_list:
    for x in range(tower.start, tower.end):
        table[x-offset] = max(table[x-offset], tower.height)

#print(table, file=sys.stderr)

#for k, g in groupby(table):
#    print(k, len(list(g)), file=sys.stderr)

h = [k for k, g in groupby(table)]
print(h, file=sys.stderr)

current_h = h[0]
block = 3
for i in range(1, len(h)):
    if current_h == 0 and h[i] > 0:
        block += 3
    elif h[i] > current_h:
        block -= 1 # remove the right wall
        block += 3
    elif h[i] == 0:
        block += 1 #floor
    elif h[i] > 0 and h[i] < current_h :
        block += 2
    current_h = h[i]

print(block)

""" 
tower_list.sort(key = lambda x:x.start)
print(tower_list, file=sys.stderr)

pieces = 0
current_x = tower_list[0].start
current_h = 0
loop = 0
for tower in tower_list:
    if tower.start > current_x:
        pieces += 1 #for the ground
        pieces += 3 #for the building
        current_x = tower.end
        current_h = tower.height
    elif tower.start < current_x:
        if current_h >= tower.height:
            pieces += 2 #roof + wall
        else:
            pieces += 3 #roof + 2 walls
        current_x = tower.end
        current_h = tower.height
    else :
        if loop != 0: pieces -= 1 #to avoid -1 in first building
        if current_h >= tower.height:
            pieces += 2 #roof + wall
        else:
            pieces += 3 #roof + 2 walls
        current_x = tower.end
        current_h = tower.height
    loop +=1 
        
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print(pieces)
"""