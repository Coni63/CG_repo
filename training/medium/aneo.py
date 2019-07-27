import sys
import math
import numpy as np

speed = int(input())
light_count = int(input())

X = np.zeros(shape=(light_count, 2), dtype=np.uint32)

for i in range(light_count):
    X[i, :] = [int(j) for j in input().split()]

for i in range(speed, 1, -1):
    time = X[:, 0]*3.6/i
    state = time % (X[:, 1]*2)
    state = (state < X[:, 1]).mean() == 1
    if state:
        print(i)
        break
