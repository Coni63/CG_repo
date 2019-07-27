import sys
import math

"""
between 100 and 200, there is 34 lucky number
between 200 and 300, there is 34 lucky number
...
between 600 and 700, there is 81 lucky number
between 800 and 900, there is 81 lucky number
...
more generally, every 10**k+1 there is 8*a_k+2*b_k 
with a_k = 8*a_k-1 + 2*b_k-1
and b_k = 9**k
"""

def countSmall(n):
    lucky = 0
    for i in range(n):
        number = str(i)
        if (number.count("6") > 0) ^ (number.count("8") > 0):
            lucky += 1
    return lucky
    
def countBig(n):
    strn = str(n)
    powers = list(range(len(strn)-1, -1, -1))
    digits = [int(x) for x in strn]
    c=0

    for digit, power in zip(digits, powers):
        for i in range(digit):
            c += factor[power-2][0]
            if i in [6, 8]:
                c += (factor[power-2][1] - factor[power-2][0])

        # print("n {} digit {} power {}, {}".format(n, k, p, c), file=sys.stderr)             
    return c

def countLucky(n):
    if n <= 1000:
        return countSmall(n)
    else:
        n1 = countSmall(n%1000)
        n2 = countBig(n - (n%1000))
        print(n1, n2, file=sys.stderr)
        return n1 + n2
    

factor = [(34, 81)]
for i in range(1, 19):
    a = 8*factor[-1][0] + 2*factor[-1][1]
    b = 9*factor[-1][1]
    factor.append((a, b, b-a))
print(factor, file=sys.stderr)

l, r = [int(i) for i in input().split()]

lucky1 = countLucky(l)
lucky2 = countLucky(r)
print(lucky2 - lucky1)

# a = 187700
# b = countBig(a)
# c = countSmall(a)
# print("N {} Sure : {} - Pred {} - diff {}".format(a, c, b, c-b))

# for a in range(59000, 89000, 1000):
#     b = countBig(a)
#     c = countSmall(a)
#     print("N {} Sure : {} - Pred {} - diff {}".format(a, c, b, c-b))
