import sys
import math
import numpy as np
from scipy import signal
import time

width, height = [int(i) for i in input().split()]
grid = [[1 if x!= "#" else 0 for x in list(input())] for _ in range(height)]

s=time.time()
X = np.array(grid)
y = np.array([[0, 1, 0], [1, 0, 1], [0, 1, 0]])

z = signal.convolve2d(X, y, mode='same')

z=z.astype(str)
z[X==0] = "#"

print(time.time()-s, file=sys.stderr)
for row in z:
    print(*row, sep="")
