import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

tab = []
n = int(input())

for i in range(n):
    v, e = [int(j) for j in input().split()]
    tab.append((v, e))
    
mini = float('inf')
for i in range(len(tab)):
    for j in range(i+1, len(tab)):
        mini = min( abs(tab[j][0]-tab[i][0])+abs(tab[j][1]-tab[i][1]) , mini)

print(mini)

"""
tab = []

n = int(input())

for i in range(n):
    v, e = [int(j) for j in input().split()]
    tab.append(v+e)
    
tab.sort()

#t = [j-i for i, j in zip(tab[:-1], tab[1:])]
#print(min(t))

mini = float('inf')

for i in range(len(tab)-1):
    mini = min(tab[i+1]-tab[i], mini)

print(mini)
"""