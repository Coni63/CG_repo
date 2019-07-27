import sys
import math
import numpy as np
from numpy.linalg import norm

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
X = np.zeros((4, 2))
n = int(input())
for i in range(n):
    a, x_a, y_a, b, x_b, y_b, c, x_c, y_c, d, x_d, y_d = input().split()
    x_a = int(x_a)
    y_a = int(y_a)
    x_b = int(x_b)
    y_b = int(y_b)
    x_c = int(x_c)
    y_c = int(y_c)
    x_d = int(x_d)
    y_d = int(y_d)
    X[0,0] = x_a
    X[1,0] = x_b
    X[2,0] = x_c
    X[3,0] = x_d
    X[0,1] = y_a
    X[1,1] = y_b
    X[2,1] = y_c
    X[3,1] = y_d
    name = a+b+c+d
    

    L = [norm(X[i, :]-X[(i+1)%4, :]) for i in range(4)]
    S = np.dot( X[0, :]-X[1, :] , X[0, :]-X[3, :] )
    print(X, file=sys.stderr)
    
    if len(set(L)) == 1:
        if S ==0:
            print("{} is a square.".format(name))
        else:
            print("{} is a rhombus.".format(name))
    elif L[0] == L[2] and L[1] == L[3]:
        if S ==0:
            print("{} is a rectangle.".format(name))
        else:
            print("{} is a parallelogram.".format(name))
    else:
        print("{} is a quadrilateral.".format(name))
