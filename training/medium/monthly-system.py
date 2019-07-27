import sys
import math

base = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
a = {month : i for i, month in enumerate(base)}
b = {i : month for i, month in enumerate(base)}

n = int(input())
total = 0
for i in range(n):
    m = input()
    slice_ = [m[i:i+3] for i in range(0, len(m), 3)]
    v = [a[x] for x in slice_]
    l = len(v)
    total += sum([x * 12**(l-i-1) for i, x in enumerate(v)])

digits = []
while total > 0:
    digits.append(total % 12)
    total //= 12
digits = digits[::-1]

for each in digits:
    print(b[each], end="")
