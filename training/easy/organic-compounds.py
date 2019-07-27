import sys
import math
import re

def split_by_n(seq, n):
    '''A generator to divide a sequence into chunks of n units.'''
    while seq:
        yield seq[:n]
        seq = seq[n:]

n = int(input())

# get input
l = []
for i in range(n):
    compound = input()
    l.append(list(split_by_n(compound, 3)))

# parse to number
numbers = []
for row in l:
    numbers.append([int(re.sub("[^0-9]", "", elem)) if len(elem.strip()) > 0 else 0 for elem in row])

# pad to max len
maxlen = max([len(x) for x in numbers])
for i in range(n):
    numbers[i] += [0] * (maxlen - len(numbers[i]))

ans = "VALID"
for i in range(0, n, 2):
    for j in range(0, maxlen, 2):
        s = numbers[i][j]
        if i > 0:
            s += numbers[i-1][j]
        if i < n-1:
            s += numbers[i+1][j]
        if j > 0:
            s += numbers[i][j-1]
        if j < maxlen-1:
            s += numbers[i][j+1]

        if s not in [0, 4]:
            ans = "INVALID"
            break

print(ans)
