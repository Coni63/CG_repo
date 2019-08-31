import sys
import math
import numpy as np

def shift(x):
    return ord(x) - ord("a") + 1

memo = {}  # (grid_rotation, pos) : turn

ii = int(input())

nb = int(input())
nb2 = nb**2

X = np.array([list(input()) for i in range(nb)])
X_flat = X.flatten()

n = 0      # postion on the flat grid
angle = 0

turn = 1
while turn < ii:
    letter = X_flat[n]
    while letter in "@#": # a rotation can lead to another symbol ... up to 4 times but this is not considered
        if letter == "#":
            X = np.rot90(X, 3) # CW
            X_flat = X.flatten()
            letter = X_flat[n]
            angle += 3
            angle %= 4
        elif letter == "@":
            X = np.rot90(X, 1) # CCW
            X_flat = X.flatten()
            letter = X_flat[n]
            angle += 1
            angle %= 4
            
    n += shift(letter)
    n %= nb2
    
    if (angle, n) in memo.keys():
        loop_size = turn - memo[(angle, n)]
        ii = turn + (ii-turn) % loop_size
    else:
        memo[(angle, n)] = turn
        
    turn += 1
    
print(X_flat[n])
