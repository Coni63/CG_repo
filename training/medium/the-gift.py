import sys
import math
from operator import itemgetter

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
arr = []
out = []
    
n = int(input())
c = int(input())

c_init = c

for i in range(n):
    b = int(input())
    arr.append(b)

print(str(n)+" payeurs", file=sys.stderr)
print(str(c_init)+" $ le cadeau", file=sys.stderr) 

if sum(arr)<c:
    print("IMPOSSIBLE")
else:
    arr.sort()
    print(arr, file=sys.stderr) 
    for i in range(n):
        avg = int(c/(n-i))
        if arr[i] <= avg:
            c-=arr[i]
            out.append(arr[i])
        else:
            c-=avg
            out.append(avg)
    
    reste = c - int(c/len(arr))*len(arr)
        
    for i in range(reste):
        out[n-i-1]+=1
  
for each in out:
    print(each)
# To debug: print("Debug messages...", file=sys.stderr)