import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
r = int(input())
tab = [[0 for _ in range(r+1)] for _ in range(n)]

price = int(input())
for i in range(r):
    tab[0][i] = price
    
for i in range(1, n):
    price = int(input())
    for j in range(r):
        tab[i][j] = price + tab[i-1][j+1]
    tab[i][r]=max(tab[i-1]);

print(max(tab[-1]))
print(tab, file=sys.stderr)
