import sys
import math
import itertools

size = {"0": 4, "1":3}

def next_term(num):
    binary = str(bin(num))[2:]
    count = 0
    for k, g in itertools.groupby(binary):
        count += len(list(g))*size[k]
    return count

S, n = [int(i) for i in input().split()]

for i in range(n):
    prev = S
    S = next_term(prev)
    if S == prev:
        break
    print(i, S, file=sys.stderr)
    
print(S)
