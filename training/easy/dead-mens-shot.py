import sys
import math

import numpy as np
from scipy.optimize import linprog

def in_hull(points, x):
    n_points = len(points)
    n_dim = len(x)
    c = np.zeros(n_points)
    A = np.r_[points.T,np.ones((1,n_points))]
    b = np.r_[x, np.ones(1)]
    lp = linprog(c, A_eq=A, b_eq=b)
    return lp.success

n = int(input())
Z = np.zeros(shape=(n, 2), dtype=int)
for i in range(n):
    Z[i] = [int(j) for j in input().split()]
    
m = int(input())
x = np.zeros(shape=(n, 2), dtype=int)
for i in range(m):
    x = np.array([int(j) for j in input().split()])
    if in_hull(Z, x):
        print("hit")
    else:
        print("miss")

