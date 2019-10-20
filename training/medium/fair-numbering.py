import sys
import math
import numpy as np

c = np.zeros(10000001, dtype=np.uint8)
c[1:10] = 1
c[10:100] = 2
c[100:1000] = 3
c[1000:10000] = 4
c[10000:100000] = 5
c[100000:1000000] = 6
c[1000000:10000000] = 7
c = np.cumsum(c)
s = set(c)

n = int(input())
for i in range(n):
    st, ed = [int(j) for j in input().split()]
    total_digit = c[ed] - c[st+1]
    half = c[st] + total_digit//2
    while half not in s:
        half -= 1
    shift = np.argwhere(c==half)
    print(shift[0][0])
