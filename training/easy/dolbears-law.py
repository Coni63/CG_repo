import sys
import math

def f1(n60):
    return 10 + (n60-40)/7

def f2(n8):
    return n8 + 5

ts = []
flat_t = []
m = int(input())
for i in range(m):
    line = [int(x) for x in input().split()]
    flat_t += line
    ts.append(f1(sum(line)))

T = sum(ts)/m
print("{:.1f}".format(T))

if 5 <= T <= 30:
    ts = []
    for i in range((15*m)//2):
        n8 = sum(flat_t[i*2:i*2+2])
        ts.append(f2(n8))
    T = sum(ts)/len(ts)
    print("{:.1f}".format(T))
