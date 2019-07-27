import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())

output = ""

if n != 0 :
    while abs(n) > 0:
        rem = n%3
        n = n//3
        if rem == 2:
            rem = -1
            n += 1 
       
        if rem == 0:
            output = "0" + output   
        elif rem == 1:
            output = "1" + output
        else:
            output = "T" + output
else:
    output = "0"
    
print(output)


# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

