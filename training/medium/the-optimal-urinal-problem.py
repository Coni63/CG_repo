import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def f(n):
    if memo[n]>-1:
        return memo[n]
    if n%2==1:
        memo[n] = 2*f((n+1)//2)-1
        return memo[n]
    else:
        half = n//2
        memo[n] = f(half)+f(half+1)-1
        return memo[n]

n = int(input())

memo = [0,1,1,2,2] + [-1]*1500000

max_person = 0
max_index = -1
for i in range(1,(n+1)//2 + 1):
    person = f(i)+f(n+1-i)-1 # recursion with memo
    if person > max_person:
        max_person = person
        max_index = i
print(max_person, max_index)

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

