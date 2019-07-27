import sys
import math
import numpy as np

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
arr = []
n = int(input())
for i in range(n):
    arr.append([int(j) for j in input().split()])
arr = np.array(arr, dtype="int8")
print(arr, file=sys.stderr)


magic = True

# verif doublons
if len(np.unique(arr)) < n*n:
    magic = False

# verif value integer
if (arr > n*n).sum() > 0:
    magic = False
    
# sum line
t = np.unique(arr.sum(axis=0))
if len(t) == 1:
    a = t[0]
else:
    a = 0
    magic = False

# sum col
t = np.unique(arr.sum(axis=1))
if len(t) == 1:
    b = t[0]
else:
    b=0
    magic = False

# check same row as col
if a != b:
    magic = False
    
# sum diag
if a != np.trace(arr):
    magic = False

# sum diag reverse
if a != np.trace(np.rot90(arr)):
    magic = False

if magic:
    print("MAGIC")  
else:
    print("MUGGLE")
