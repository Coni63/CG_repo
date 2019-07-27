import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def fact(n):
    """fact(n): calcule la factorielle de n (entier >= 0)"""
    x=1
    for i in range(2,n+1):
        x*=i
    return x

def C(p, n):
    return fact(n)//(fact(p)*fact(n-p))

m = int(input())-1
n = int(input())-1

tot = str(C(n, n+m))
length = len(tot)

if length > 1000:
    tot = tot[:1000]#+"0"*(length-1000)
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print(tot)
