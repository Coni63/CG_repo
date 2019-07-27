import sys
import math
import itertools
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

pts = [5, 2, 3]
choice = list(range(40))
n = int(input())

# To debug: print("Debug messages...", file=sys.stderr)

for subset in itertools.product(choice, repeat=3):
    if subset[1] <= subset[0]: #on retire les combinaison ou on transforme plus que l'on try
        somme = sum(list(subset[i]*pts[i] for i in range(3)))
        #print(subset, file=sys.stderr)
        #print(somme, file=sys.stderr)
        if somme == n:
            result = [str(i) for i in subset]
            print(" ".join(result))

