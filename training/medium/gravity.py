import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
mapping = []

width, height = [int(i) for i in input().split()]
for i in range(height):
    line = input()
    print(line.split(), file=sys.stderr)
    mapping.append(line)

for n in range(height):
    for y in range(height-1):
        for x in range(width):
            if mapping[y][x]=="#" and mapping[y+1][x] == ".":
                mapping[y] = mapping[y][:x] + '.' + mapping[y][x+1:]
                #mapping[y][x] = "."
                mapping[y+1] = mapping[y+1][:x] + '#' + mapping[y+1][x+1:]
                a =1 
            
            

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
for y in range(height):
    print(mapping[y])
