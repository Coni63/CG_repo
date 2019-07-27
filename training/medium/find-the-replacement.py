import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

x = input()
y = input()


replacements = {}
flag = True

for a, b in zip(x, y):
    if a != b:
        if replacements.get(a, None) is None:
            replacements[a] = b
        else:
            if replacements[a] != b:
                print("CAN'T")
                flag = False
                break
        
if flag:
    if len(replacements) > 0:
        for x, y in replacements.items():
            print("{}->{}".format(x, y))
    else:
        print("NONE")
