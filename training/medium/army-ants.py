import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n1, n2 = [int(i) for i in input().split()]
n = n1 + n2

s1 = list(input())
s2 = list(input())
seq = s1[::-1]+s2

t = int(input())

for _ in range(t):
    i = 0
    while i < n-1:
        if seq[i] in s1 and seq[i+1] in s2:
            seq[i] , seq[i+1] = seq[i+1] , seq[i]
            i += 1
        i += 1

print("".join(seq))
