import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

type_block = {0:{"BLOCK":"BLOCK"}, 
        1:{"RIGHT":"BOTTOM", "LEFT":"BOTTOM", "TOP":"BOTTOM"},
        2:{"RIGHT":"LEFT", "LEFT":"RIGHT"}, 
        3:{"TOP":"BOTTOM"}, 
        4:{"TOP":"LEFT", "RIGHT":"BOTTOM"}, 
        5:{"TOP":"RIGHT", "LEFT":"BOTTOM"}, 
        6:{"RIGHT":"LEFT", "LEFT":"RIGHT"}, 
        7:{"RIGHT":"BOTTOM", "TOP":"BOTTOM"}, 
        8:{"RIGHT":"BOTTOM", "LEFT":"BOTTOM"}, 
        9:{"LEFT":"BOTTOM", "TOP":"BOTTOM"}, 
        10:{"TOP":"LEFT"}, 
        11:{"TOP":"RIGHT"}, 
        12:{"RIGHT":"BOTTOM"}, 
        13:{"LEFT":"BOTTOM"}
        }

invert = {"RIGHT":"LEFT", "LEFT":"RIGHT", "BOTTOM":"TOP"}

arr = []

# w: number of columns.
# h: number of rows.
w, h = [int(i) for i in input().split()]
for i in range(h):
    line = input()  # represents a line in the grid and contains W integers. Each integer represents one room of a given type.
    print(line, file=sys.stderr)
    arr.append(line.split(" "))
    
ex = int(input())  # the coordinate along the X axis of the exit (not useful for this first mission, but must be read).

# game loop
while True:
    xi, yi, pos = input().split()
    xi = int(xi)
    yi = int(yi)
    
    block = int(arr[yi][xi])
    print(block, file=sys.stderr)
    
    out_direction = type_block[block][pos]
    print(out_direction, file=sys.stderr)
    
    if out_direction == "BOTTOM":
        print(xi, yi+1)
    elif out_direction == "LEFT":
        print(xi-1, yi)
    elif out_direction == "RIGHT":
        print(xi+1, yi)

    # To debug: print("Debug messages...", file=sys.stderr)
