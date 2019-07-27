import sys
import math

w, h = [int(i) for i in input().split()]

a = []
for i in range(h):
    a.append(list(map(int, input().split())))

for i in range(h):
    for j in range(w):
        if i == 0 and j == 0:
            pass
        else:
            if i == 0:
                a[i][j] += a[i][j-1]
            elif j == 0:
                a[i][j] += a[i-1][j]
            else:    
                a[i][j] += max(a[i-1][j], a[i][j-1]) 

    
print(a[-1][-1])


