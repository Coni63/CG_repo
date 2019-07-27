import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
point = []
list_x = []
list_y = []

n = int(input())
if n > 0:
    for i in range(n):
        x, y = [int(j) for j in input().split()]
        point.append([x,y])
        list_x.append(x)
        list_y.append(y)
        
    min_x = min(min(list_x)-1,-1)
    max_x = max(max(list_x)+1, 1)
    min_y = min(min(list_y)-1,-1)
    max_y = max(max(list_y)+1, 1)
    
    width = max_x-min_x+1
    height = max_y-min_y+1
    
    for y in range(height):
        res = ""
        for x in range(width):
            offset_x = x + min_x 
            offset_y =max_y - y 
            if [offset_x, offset_y] in point:
                res += "*"
            else:
                if offset_x != 0 and offset_y == 0:
                    res += "-"
                elif offset_x == 0 and offset_y == 0:
                    res += "+"
                elif offset_x == 0 and offset_y != 0:
                    res += "|"
                else:
                    res += "."
        print(res)
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
    
else:
    print(".|.")
    print("-+-")
    print(".|.")
