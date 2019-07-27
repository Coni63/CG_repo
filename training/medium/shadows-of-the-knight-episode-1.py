import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]

min_x = 0
max_x = w
max_y = 0
min_y = h

pos_x = x0
pos_y = y0

print(str(w) + " - " + str(h), file=sys.stderr)

# game loop
while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)
    print(bomb_dir, file=sys.stderr)
    
    delta_x = 0
    delta_y = 0
    
    if "U" in bomb_dir:
        delta_y = -math.ceil((pos_y-max_y)/2) #- car on monte
        min_y = pos_y
        
    if "D" in bomb_dir:
        delta_y = math.ceil((min_y-pos_y)/2)
        max_y = pos_y
        
    if "L" in bomb_dir:
        delta_x = -math.ceil((pos_x-min_x)/2)
        max_x=pos_x
        
    if "R" in bomb_dir:    
        delta_x = math.ceil((max_x-pos_x)/2)
        min_x=pos_x
      
    pos_x += delta_x
    pos_y += delta_y
    
    if pos_x<0:
        pos_x = 0
    if pos_x>=w-1:
        pos_x = w-1
    if pos_y<0:
        pos_y = 0
    if pos_y>=h-1:
        pos_y = h-1 
        
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

    # the location of the next window Batman should jump to.
    print(str(pos_x)+" "+str(pos_y))
