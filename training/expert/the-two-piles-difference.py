import sys
from math import factorial
from itertools import combinations
from operator import mul
from functools import reduce
from time import time
import random

n = int(input())
values = [int(x) for x in input().split()]
print(values, file=sys.stderr)

if n < 30:
    nb = int((factorial(n) / pow(factorial(n//2), 2))//2)
    
    listA = []
    listB = []
    
    """
    l = 0
    for item in combinations(values, n//2):
        if l < nb:
            listA.append(item)
        else:
            listB.append(item)
        l += 1
    """
    comb = list(combinations(values, n//2))
    listA = comb[:nb]
    listB = comb[nb:]
    
    diff = 1E6
    for i in range(nb):
        temp = abs(pow(sum(listA[i]), 2)-reduce(mul, listB[-i-1]))
        temp2 = abs(pow(sum(listB[i]), 2)-reduce(mul, listA[-i-1]))
        diff = min(temp, temp2, diff)
    
    print(diff)
else:
    listA = values[:n//2]
    listB = values[n//2:]
    diff = 90000
    s = time()
    while time()-s < 0.9:
        temp = abs(pow(sum(listA), 2)-reduce(mul, listB))
        temp2 = abs(pow(sum(listB), 2)-reduce(mul, listA))
        diff = min(temp, temp2, diff)
        indexA = random.randrange(n//2)
        indexB = random.randrange(n//2)
        listA[indexA], listB[indexB] = listB[indexB], listA[indexA]
    print(diff)
        