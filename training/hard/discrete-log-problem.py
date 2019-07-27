import sys
import math
import time
    
def bsgs(a, c, P):
    
    N = math.ceil(math.sqrt(P - 1))

    memo = {}
    ai = 1
    for i in range(N):
        memo[ai] = i
        ai = (a*ai) % P

    d = pow(a, N * (P - 2), P)     # https://en.wikipedia.org/wiki/Modular_multiplicative_inverse#Using_Euler.27s_theorem

    for j in range(N):
        y = (c * pow(d, j, P)) % P
        if y in memo:
            return j * N + memo[y]

    return None

a, c, p = [int(x) for x in input().split()] 

s = time.time()

if a == c:
    print(1)
else:
    ans = bsgs(a, c, p)
    if ans is None:
        print(-1)
    else:
        print(ans)

print(time.time()-s, file=sys.stderr)
