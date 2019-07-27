import sys
import math

memo = {}

def syracuse(n):
    loop = 0
    while n > 1:
        if n in memo:
            return memo[n] + loop
        else:
            if n % 2 == 0:
                n //= 2
            else:
                n = 3 * n +1
            loop += 1
    return loop + 1

n = int(input())
for i in range(n):
    a, b = [int(j) for j in input().split()]
    x = list(range(b, a-1, -1))
    maxi = 0
    idx = 0
    for num in x:
        k = syracuse(num)
        memo[num] = k
        if k >= maxi:
            maxi = k
            idx = num
    print(idx, maxi)
