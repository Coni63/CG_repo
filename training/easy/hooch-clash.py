import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

a, b = [int(i) for i in input().split()]
c, d = [int(i) for i in input().split()]

v_tot = c**3 + d**3
s_tot = c**2 + d**2

r_max = int(v_tot**(1/3))+1
r_min = int((v_tot/2)**(1/3))

r_max = min(r_max, b)
r_min = max(r_min, a)

r_cubed = {x**3:x for x in range(a, b)}

sols = []

for r_1 in range(r_min, r_max+1):
    v_missing = v_tot - r_1**3
    if v_missing in r_cubed:
        r_2 = r_cubed[v_missing]
        s_diff = abs(r_1**2-r_2**2)
        r_1, r_2 = min(r_2, r_1), max(r_2, r_1)
        fun = 1-int((r_1, r_2) == (c,d))
        sols.append((fun, s_diff, r_1, r_2))

sols.sort(key = lambda x:(x[0], x[1]), reverse=True)
print(sols, file=sys.stderr)

fun, diff, e, f = sols[0]
if fun == 0:
    print("VALID")
else:
    print(e, f)
    

