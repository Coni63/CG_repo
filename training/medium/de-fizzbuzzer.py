import sys
import math

def div_count(x, d):
    n = 0
    while True:
        if x % d == 0:
            x //= d
            n += 1
        else:
            break
    return n

def fizzbuzz(x):
    r =""
    if "3" in str(x):
        r+= "Fizz" * str(x).count("3")
    if x % 3 == 0:
        r+= "Fizz" * div_count(x, 3)
    if "5" in str(x):
        r+= "Buzz" * str(x).count("5")
    if x % 5 == 0:
        r+= "Buzz" * div_count(x, 5)
        
    if r == "":
        return str(x)
    else:
        return r

# l = {fizzbuzz(k):k for k in range(1, 1000)}
# print(l, file=sys.stderr)

l = [fizzbuzz(k) for k in range(1, 1000)]

n = int(input())
for i in range(n):
    row = input()
    try:
        print(l.index(row)+1)
    except:
        print("ERROR")


