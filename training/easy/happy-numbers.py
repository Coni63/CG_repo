import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
for i in range(n):
    x = input()
    y = sum([int(n)**2 for n in str(x)])
    loop = 1
    happy = False
    while loop < 100:
        if y == 1:
            happy = True
            break
        y = sum([int(n)**2 for n in str(y)])
        loop += 1
    if happy:
        print("{} :)".format(x))
    else:
        print("{} :(".format(x))

