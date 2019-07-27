import sys
import math
import numpy as np
from scipy.signal import convolve2d

filtre = np.array([[1, 1, 1], [1, -8, 1],[1, 1, 1]]) 

w = int(input())
h = int(input())

board = np.zeros(shape=(h, w), dtype = np.uint8)

for i in range(h):
    for j, val in enumerate(input().split()):
        board[i, j] = int(val)

conv = convolve2d(board, filtre, mode="same", fillvalue=1)

for y, x in np.argwhere(conv==8):
    print(x, y)
