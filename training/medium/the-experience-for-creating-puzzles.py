import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

xp_table = [int(10*x*math.sqrt(x)) for x in range(0, 101)]
print(xp_table, file=sys.stderr)
print(" ", file=sys.stderr)

level = int(input())
xp = int(input())
n = int(input())

print("level : %s - xp_manquant : %s - puzzle : %s" %(level, xp, n), file=sys.stderr)

total_xp = sum(xp_table[0:level+1])
print("XP total pour niveau suivant : %s" %total_xp, file=sys.stderr)

total_xp -= xp
print("XP total acquis : %s" %total_xp, file=sys.stderr)

total_xp_after_puzzle = total_xp + 300*n
print("XP apres puzzles : %s" %total_xp_after_puzzle, file=sys.stderr)

xp_restant = total_xp_after_puzzle
lvl = 0

print(" ", file=sys.stderr)

while xp_restant > xp_table[lvl]:
    xp_restant -= xp_table[lvl]
    lvl +=1
    print("level up ! (level %s - XP restant : %s)" %(lvl, xp_restant), file=sys.stderr)

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
print(lvl)
print(xp_table[lvl]-xp_restant)
