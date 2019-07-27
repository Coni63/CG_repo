import sys
import math

def is_prime(n):
    for i in range(3, n):
        if n % i == 0:
            return False
    return True

def is_carmichael(nb, i):
    if pow(i,nb,nb) == i:
        return True
    else:
        return False

n = int(input())

if not is_prime(n):
    if is_carmichael(n, 11): #vrai pour tout entier, 11 is random
        print("YES")
    else:
        print("NO")
else:
    print("NO")
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)


