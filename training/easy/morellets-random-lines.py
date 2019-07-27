import sys
import math

def pgcd(a, b, c):
    if b==0:
        if c%a == 0:
            return a
        else:
            return False
    else:
        r = a % b
        return pgcd(b,r, c)

state = 1
r = None
all_slopes = []
x_a, y_a, x_b, y_b = [int(i) for i in input().split()]

n = int(input())
for i in range(n):
    a, b, c = [int(j) for j in input().split()]
    divisor = pgcd(a, b, c)
    if divisor != False:
        a, b, c = a//divisor, b//divisor, c//divisor
    if (a,b,c) in all_slopes:
        continue
    else:
        all_slopes.append((a,b,c))
    sa = a*x_a + b*y_a + c
    sb = a*x_b + b*y_b + c
    print(sa, sb, file=sys.stderr)
    s = sa * sb
    if s == 0:
        r = "ON A LINE"
        break
    elif s < 0:
        state *= -1

if r is None:
    if state > 0:
        print("YES")
    else:
        print("NO")
else:
    print(r)
