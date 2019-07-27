import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

level = 1
total = 1

line = {}
line[0] = " *** "
line[1] = " * * "
line[2] = " * * "
line[3] = "*****"

n = int(input())

while total + level < n:
    level += 1
    total += level
    print("lvl : %s - total : %s" % (level, total), file=sys.stderr)


for i in range(4*level):
    etage = int(i/4)
    niveau = i%4
    #print("building level %s of floor %s" % (niveau, etage), file=sys.stderr)
    motif = " ".join([line[niveau] for _ in range(etage+1)])
    shift = " "*(3*(level - 1 - etage))
    #print(line, file=sys.stderr)
    print(shift+motif+shift)

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

