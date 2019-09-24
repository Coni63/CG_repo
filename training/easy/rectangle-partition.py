import sys
import math
from collections import Counter

def combine(x, maxi=1e6):
    comb = x[:]
    for i, start_x in enumerate(x):
        l = start_x
        for stop_x in x[i+1:]:
            l += stop_x
            if l <= maxi:
                comb.append(l)
            else:
                break
    c = Counter(comb)
    # print(c.most_common(3), file=sys.stderr)
    return dict(c)
            

w, h, count_x, count_y = [int(i) for i in input().split()]

x = [0] + [int(i) for i in input().split()] + [w]
y = [0] + [int(i) for i in input().split()] + [h]

offset_h = [b-a for a, b in zip(x[:-1], x[1:])]
offset_v = [b-a for a, b in zip(y[:-1], y[1:])]

print(x, offset_h, file=sys.stderr)
print(y, offset_v, file=sys.stderr)

comb_h = combine(offset_h, maxi = h)  # create all combination of horizontal parts smaller than h
comb_v = combine(offset_v, maxi = w)  # create all combination of vertical parts smaller than w

### Too slow approach (O(m*n))
# num_squares = sum([a==b for a in comb_h for b in comb_v])

### Faster approach with groupping and looping over smallest dim
num_squares = 0
if len(comb_h) < len(comb_v):
    for key, val in comb_h.items():
        num_squares += val * comb_v.get(key, 0)
else:
    for key, val in comb_v.items():
        num_squares += val * comb_h.get(key, 0)

print(num_squares)
