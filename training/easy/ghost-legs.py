import sys
import math

dico = {}

max_x = 0
w, h = [int(i) for i in input().split()]
for i in range(h):
    if i == 0:
        name = input().split()
    elif i == h-1:
        number = input().split()
    else:
        line = input().split("|")
        for j, char in enumerate(line):
            if char == "--":
                 dico[(i, j)] = (i, j+1)
                 dico[(i, j+1)] = (i, j)
                 max_x = max(max_x, j+1)
    
for x in range(max_x):
    current_column = x+1
    for y in range(h):
        if (y, current_column) in dico.keys():
            current_column = dico[(y, current_column)][1]
    print(name[x] + number[current_column-1])
