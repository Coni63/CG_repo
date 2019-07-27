import sys
import math
import copy
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


order = input()
side = input()

pli = {"U":1 , "D":1 , "L":1 , "R":1 }

for each in order:
    c = copy.deepcopy(pli)
    if each == "U" :
        pli =   {
                "U": 1, 
                "D": c["D"]+c["U"], 
                "L": 2*c["L"], 
                "R": 2*c["R"] 
                }
    elif each == "D":
        pli =   {
                "U": c["U"]+c["D"], 
                "D": 1, 
                "L": 2*c["L"], 
                "R": 2*c["R"] 
                }
    elif each == "L" :
        pli =   {
                "U": 2*c["U"], 
                "D": 2*c["D"], 
                "L": 1, 
                "R": c["R"]+c["L"]
                }
    else:
        pli =   {
                "U": 2*c["U"], 
                "D": 2*c["D"], 
                "L": c["L"]+c["R"], 
                "R":1 
                }
    print(pli, file=sys.stderr)
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print(pli[side])
