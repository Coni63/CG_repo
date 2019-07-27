import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

r_1 = int(input())
r_2 = int(input())

def next_river(x):
    diff = sum([int(y) for y in str(x)])
    return x + diff

while True:
    if r_1 < r_2:
        r_1 = next_river(r_1)
    elif r_1 > r_2:
        r_2 = next_river(r_2)
    elif r_1 == r_2:
        print(r_1)
        break
            
    
