import sys
import math

# https://www.justquant.com/numbertheory/highest-power-of-a-number-in-a-factorial/
def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

a, b = [int(i) for i in input().split()]

f = prime_factors(a)
print(f, file=sys.stderr)

g = [(value, f.count(value)) for value in set(f)]
h = []

for value, power in g:
    b2 = b
    highest_power = 0
    for i in range(1, 20):
        b2 = b2//value
        highest_power += b2
        # k = int(b/value**i)
        # highest_power += k
    h.append(int(highest_power/power))
    
print(min(h))
