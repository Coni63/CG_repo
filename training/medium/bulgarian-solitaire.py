import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
configs = []

n = int(input())
c = [int(x) for x in input().split()]

digit = sorted([x for x in c if x > 0]) #sorted([y for x in c for y in str(x) if x > 0])
configs.append(digit)

loop = 0
while True:
    k = sum([x>0 for x in c])

    c = [max(x-1, 0) for x in c] + [k]
    digit = sorted([x for x in c if x > 0])

    if digit in configs:
        res = loop - configs.index(digit) + 1
        break
        
    configs.append(digit)
    loop += 1
    
print(res)
