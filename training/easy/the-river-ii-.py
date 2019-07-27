import sys
import math

def next_river(x):
    diff = sum([int(y) for y in str(x)])
    return x + diff

r_1 = int(input())

c = 0
for i in range(1, r_1):
    print(i, next_river(i), file=sys.stderr)
    if next_river(i) == r_1:
        c+=1

if c >= 1:
    print("YES")
else:
    print("NO")
    
