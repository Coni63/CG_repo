import sys
import math

a = complex(input().replace("i", "j"))
m = int(input())

for i in range(m):
    if i == 0:
        r = a
    else:
        r = pow(r, 2) + a
    
    if r.real**2 + r.imag**2 > 4:
        break
print(i+1)
    
    




