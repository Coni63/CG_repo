import sys
import math

from queue import LifoQueue

def queue_to_list(q):
    res = []
    while not q.empty():
        res.append(q.get())
    res = res[::-1]
    while len(res)<n:
        res.append(0)
    return res
        
def step(N, beg, aux, end, count):
    if N == 1:
        print(f"{beg}=>{end}", file=sys.stderr)
        disk = mapping[beg].get()
        mapping[end].put(disk)
        return count + 1
    else:
        count = step(N-1, beg, end, aux, count)
        if count == t:
            return count
        count = step(1, beg, aux, end, count)
        if count == t:
            return count
        count = step(N-1, aux, beg, end, count)
        return count
    

n = int(input())
t = int(input())

## Queue preparation

total_step = 2**n - 1

a = LifoQueue()
b = LifoQueue()
c = LifoQueue()

for i in range(n, 0, -1):
    a.put(i)

mapping = {"A": a, "B": b, "C":c}

## Solving -- https://www.youtube.com/watch?v=5_6nsViVM00

_ = step(n, "A", "B", "C", 0)

a = queue_to_list(a)
b = queue_to_list(b)
c = queue_to_list(c)

print(a, file=sys.stderr)
print(b, file=sys.stderr)
print(c, file=sys.stderr)

## Drawing

space = 2*n+1
for i in range(n):
    if a[-i-1] == 0:
        print(" " * n + "|" + " " * n, end=" ")
    else:
        r = a[-i-1]
        print(" " * (n-r) + "#" * (2*r+1) + " " * (n-r), end=" ")
        
    if b[-i-1] == 0:
        print(" " * n + "|" + " " * n, end=" ")
    else:
        r = b[-i-1]
        print(" " * (n-r) + "#"*(2*r+1) + " " * (n-r), end=" ")
        
    if c[-i-1] == 0:
        print(" " * n + "|")
    else:
        r = c[-i-1]
        print(" " * (n-r) + "#"*(2*r+1))
        
print(total_step)
