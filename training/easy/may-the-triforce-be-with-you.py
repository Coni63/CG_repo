import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def triforce(height):
    count_top = 0
    nb = 0
    for i in range(1, height*2, 2):
        nb = i
        if count_top == 0:
            line = "."+" "*(height-2+height)+"*"*nb
        else:
            line = " "*(height-count_top-1+height)+"*"*nb
        count_top+=1    
        print(line)
    
    count_top = 0
    nb = 1
    for j in range((height+1)*2, height*4+2, 2):
        line = " "*(height-count_top-1)+"*"*nb+" "*(2*(height-count_top-1)+1)+"*"*nb
        nb += 2
        count_top+=1    
        print(line)

n = int(input())
triforce(n)
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

