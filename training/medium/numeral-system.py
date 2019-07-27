import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

equality = input()

pos_plus = equality.index("+")
pos_egal = equality.index("=")

a = equality[:pos_plus]
b = equality[pos_plus+1:pos_egal]
c = equality[pos_egal+1:]

for base in range(2, 37):
    try:
        x = int(a, base)
        y = int(b, base)
        z = int(c, base)
        if str(x+y) == str(z):
            print(base)
            break
    except:
        pass
