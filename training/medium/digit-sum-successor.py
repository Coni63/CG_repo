import sys
import math


def getnext(arr): 
    # first non 0 value
    i = len(arr) - 1
    while (arr[i] == 0): 
        i-=1
    n = i
    
    # second non 9 value
    i-=1
    while (arr[i] == 9): 
        i-=1; 
    m = i
    
    # increment
    arr[n] -= 1
    arr[m] += 1
    
    # sort of the end of the number
    if arr[0] == 0:
        start = arr[1:m+1]
    else:
        start = arr[:m+1]
    stop = sorted(arr[m+1:])
    
    return start+stop
    
arr =  [0] + [int(x) for x in input()]
  
res = getnext(arr)

print(*res, sep=""); 
