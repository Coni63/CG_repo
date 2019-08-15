import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())

start = list(range(1, n+1))
elem = start[:]
suite = []
for i in range(n):
    new_elem = []
    if n%2 == 0:
        for j in range(n//2):
            new_elem.append(elem[-j-1])
            new_elem.append(elem[j])
        elem = new_elem
    else:
        for j in range((n+1)//2):
            new_elem.append(elem[-j-1])
            new_elem.append(elem[j])
        elem = new_elem[:-1]
    suite.append(elem)
    
if elem == start:
    for each in suite:
        print(",".join([str(x) for x in each]))
else:
    print("IMPOSSIBLE")
