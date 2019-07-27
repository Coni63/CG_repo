import sys
import math

width = int(input())  # the number of cells on the X axis
height = int(input())  # the number of cells on the Y axis

def recherche(sens, line, col):
    global arr , width, height
    if sens == "Horizontal":
        for x in range(col+1, width):
            if arr[line][x] == "0":
                return  " "+str(x)+" "+str(line)
    else:
        for y in range(line+1,height):
            if arr[y][col] == "0":
                return " "+str(col)+" "+str(y)
    return " -1 -1"

arr = []

for i in range(height):
    line = input()  # width characters, each either 0 or .
    arr.append(list(line))
            
for each_line in range(height):
    for each_col in range(width):
        if arr[each_line][each_col]=="0": #si c'est un noeud
            res = str(each_col)+" "+str(each_line)
            res += recherche("Horizontal", each_line, each_col)
            res += recherche("Vertical", each_line, each_col)
            print(res)  
            
# To debug: print("Debug messages...", file=sys.stderr)