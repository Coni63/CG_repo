import sys
import math

def getFactors(n):
    nn = n * n
    factors = []
    for i in range(1, n+1):
        if nn % i == 0: factors.append(i)
    return factors

def process(n):
    abList = []
    nn = n * n;
    factors = getFactors(n)
    for factor in factors:
        a = nn // factor
        aa = a + n
        bb = factor + n
        abList.append((aa, bb))
    return abList
        
        
n = int(input())
abList = process(n)
print(abList, file=sys.stderr)
for aa, bb in abList:
    print(f"1/{n} = 1/{aa} + 1/{bb}")
