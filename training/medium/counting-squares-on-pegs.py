import sys
import math

import numpy as np
from scipy.spatial.distance import pdist, squareform
from collections import Counter
import time


n = int(input())

# X = np.zeros(shape = (n,2))
hashmap = {}
points = []

for i in range(n):
    x, y = [int(j) for j in input().split()]
    # X[i, 0] = x
    # X[i, 1] = y
    points.append((x, y))
    hashmap[hash((x, y))] = (x, y)

start = time.time()

#### V1 

# distances = pdist(X)

# counter = Counter(distances)

# possible = 0
# for value, freq in counter.most_common():
#     if freq >= 4:
#         t = counter[value * math.sqrt(2)]
#         if t >= 2:
#             possible += min(freq-3, t//2)
#     else:
#         break

# print(possible)

#### V2
count = 0
for i in range(n):
    for j in range(n):
        if i != j :
            a = points[i]
            b = points[j]
            
            midX = (a[0] + b[0])/2
            midY = (a[1] + b[1])/2
            
            Ax = a[0] - midX
            Ay = a[1] - midY
            
            Bx = b[0] - midX
            By = b[1] - midY
            
            #c = (midX + midY - a[1], midY + midX - a[0])
            #d = (midX + midY - c[1], midY - midX + c[0])
            
            c = (midX - Ay, midY + Ax)
            d = (midX - By, midY + Bx)
            
            if hash(c) in hashmap.keys() and hash(d) in hashmap.keys():
                count += 1

print(count//4)


print(time.time()-start, file=sys.stderr)
