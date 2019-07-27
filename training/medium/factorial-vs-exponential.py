import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

"""
On passe au log on a :
n * log(a) < sum(log(i) pour i de 1 à n)
"""

r = []
k = int(input())
for i in input().split():
    a = float(i)
    n = 2
    current_list = math.log(2)
    while current_list < n * math.log(a):
        n += 1
        current_list += math.log(n)
    r.append(n)
    
print(" ".join(map(str, r)))


# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)


