import sys
import math
import numpy as np

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
words = []
n = int(input())
for i in range(n):
    w = np.array(list(input()))
    words.append(w)

m = []
h, w = [int(i) for i in input().split()]
for i in range(h):
    line = list(input())
    m.append(line)
    
m = np.array(m)
result = np.zeros(shape=(h, w))

for word in words:
    # word = words[0]
    a = len(word)
    
    # check lines
    for i in range(h):
        for j in range(w-a+1):
            if np.array_equal(m[i, j:j+a], word) or np.array_equal(m[i, j:j+a], word[::-1]):
                result[i, j:j+a] = 1
                
    # check cols
    for i in range(w):
        for j in range(h-a+1):
            if np.array_equal(m[j:j+a, i], word) or np.array_equal(m[j:j+a, i], word[::-1]):
                result[j:j+a, i] = 1

    # check diag
    perm = min(w, h)-1
    for i in range(-perm, perm+1):
        diag = np.diagonal(m, i)
        if len(diag) >= a:
            for j in range(len(diag)-a+1):
                if np.array_equal(diag[j:j+a], word) or np.array_equal(diag[j:j+a], word[::-1]):
                    print(diag, file=sys.stderr)
                    for k in range(a):
                        result[j+k, j+k+i] = 1
    
    m = np.rot90(m, 1)
    result = np.rot90(result, 1)
    perm = min(w, h)-1
    for i in range(-perm, perm+1):
        diag = np.diagonal(m, i)
        if len(diag) >= a:
            for j in range(len(diag)-a+1):
                if np.array_equal(diag[j:j+a], word) or np.array_equal(diag[j:j+a], word[::-1]):
                    print(diag[j:j+a], word, file=sys.stderr)
                    for k in range(a):
                        result[j+k, j+k+i] = 1
    
    m = np.rot90(m, 3)
    result = np.rot90(result, 3)
                    
print("".join(m[result == 0]))

