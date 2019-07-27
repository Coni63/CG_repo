import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

i = 1
while True:
    if i*(i+1)/2 >= n :
        print(i)
        break
    else:
        i +=1
