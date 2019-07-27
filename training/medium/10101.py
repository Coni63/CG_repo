import sys
import math
import numpy as np
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

w = int(input())
h = int(input())

filter_ = np.matrix([[0,0],[0,0]])

carte = []
for i in range(h):
    row = input()
    line = []
    for letter in row:
        if letter == ".":
            line.append(1)
        else:
            line.append(0)
    carte.append(line)

carte = np.matrix(carte)
# print(carte, file=sys.stderr)
# print(filter_, file=sys.stderr)

s = 0
for x in range(w-1):
    for y in range(h-1):
        part = carte[y:y+2, x:x+2]
        if np.sum(part) == 4:
            carte_fill = carte.copy()
            carte_fill[y:y+2, x:x+2] = filter_
            sum_col = np.sum(carte_fill, axis=0)
            sum_row = np.sum(carte_fill, axis=1)
            a = np.sum(sum_row == 0) + np.sum(sum_col == 0)
            s = max(s,a)
print(s)
