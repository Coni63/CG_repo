import sys
import math

def leaves_elim(Pairs):
    M = len(Pairs)
    Q = [i for i in range(M) if len(Pairs[i])==1]
    Sol = [None]*M
    while Q:
        u = Q.pop()
        if Pairs[u]:
            assert len(Pairs[u])==1
            v = Pairs[u].pop()
            Sol[u], Sol[v] = v, u
            while Pairs[v]:
                w = Pairs[v].pop()
                if w!=u:
                    Pairs[w].remove(v)
                    if len(Pairs[w])==1:
                        Q.append(w)
    return Sol

n, t = [int(i) for i in input().split()]
m = 2*n
Pairs = [set(range(1-i%2, m, 2)) for i in range(m)]
for _ in range(t):
    Conf = [int(c)-1 for c in input().split()]
    Even, Odd = [], []
    for c in Conf:
        (Even if c%2==0 else Odd).append(c)
    for e in Even:
        for o in Odd:
            Pairs[e].discard(o)
            Pairs[o].discard(e)
Sol = leaves_elim(Pairs)
assert None not in Sol
print(*(Sol[i]+1 for i in range(0,m,2)))

# # Write an action using print
# # To debug: print("Debug messages...", file=sys.stderr)

# print("2 4 6...")
