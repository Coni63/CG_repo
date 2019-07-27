import sys
import math
from time import time
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n, m, seed = [int(i) for i in input().split()]

start = time()
horse_list = []

y = None
for i in range(m):
    if i == 0:
        x = seed
    else:
        x = (1103515245 * y + 12345) % 2147483648
    y = (1103515245 * x + 12345) % 2147483648
    horse_list.append( (x, y) )
    
for _ in range(n):
    v, e = [int(j) for j in input().split()]
    horse_list.append((v, e))


print(time() - start, file=sys.stderr)


mini = 2**31

if n+m < 2000:
    for i in range(n+m):
        for j in range(i+1, n+m):
            mini = min( abs(horse_list[j][0]-horse_list[i][0])+abs(horse_list[j][1]-horse_list[i][1]) , mini)
else:
    horse_list.sort(key=lambda tup: tup[0])
    for i in range(n+m):
        for j in range(i+1, n+m):
            if horse_list[j][0]-horse_list[i][0] < 200000:
                mini = min( abs(horse_list[j][0]-horse_list[i][0])+abs(horse_list[j][1]-horse_list[i][1]) , mini)
            else:
                break

print(mini)

print(time() - start, file=sys.stderr)