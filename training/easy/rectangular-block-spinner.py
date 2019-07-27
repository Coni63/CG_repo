import sys
import math
import numpy as np
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

size = int(input())
steps = (int(input()) % 360)//45
print(steps, file=sys.stderr)
height = size + size - 1

square = [list(input().replace(" ", "")) for i in range(size)]
square = np.array(square)
print(square, file=sys.stderr)

if steps == 1:
    for i in range(height):
        word = np.diagonal(square, offset=(size-i-1), axis1=0, axis2=1)  # this diag \
        word = " ".join(word)
        print(('{: ^' + str(height) + '}').format(word))

if steps == 3:
    for i in range(height):
        word = np.diagonal(np.rot90(square), offset=(size-i-1), axis1=0, axis2=1)
        word = " ".join(word)
        print(('{: ^' + str(height) + '}').format(word))

if steps == 5:
    for i in range(height):
        word = np.diagonal(square, offset=-(size-i-1), axis1=0, axis2=1)
        word = " ".join(word)
        print(('{: ^' + str(height) + '}').format(word))

if steps == 7:
    for i in range(height):
        word = np.diagonal(np.rot90(square), offset=-(size-i-1), axis1=0, axis2=1)
        word = " ".join(word)[::-1]
        print(('{: ^' + str(height) + '}').format(word))
