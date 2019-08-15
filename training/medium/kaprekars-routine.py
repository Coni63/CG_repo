import sys
import math

def d(x):
    a = reversed(sorted(list(x)))
    return "".join(a)

def a(x):
    a = sorted(list(x))
    return "".join(a)

n = input()
res = [n]
f = "{:0" + str(len(n)) + "d}"
while True:
    n = int(d(n)) - int(a(n))
    n = f.format(n)
    if n in res:
        break
    else:
        res.append(n)
idx = res.index(n)
print(*res[idx:])
