import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())

def divisorGenerator(n):
    large_divisors = 0
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            large_divisors += i
            if i*i != n:
                large_divisors += int(n / i)
    return large_divisors

s = 0
for i in range(1, n+1):
    s += divisorGenerator(i)
    
#print(list_of_divisor, file=sys.stderr)
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print(s)
