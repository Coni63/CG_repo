import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def convert(letter, number):
    r = 0
    for i in range(4):
        r += (ord(letter[i]) - ord('A')) * (26**(3-i))
    r = r * 999 + number
    return r

def convert_reverse(num):
    reste = '{:03d}'.format(num % 999)
    num = num // 999
    mot = ""
    for i in range(4):
        offset = num // (26**(3-i))
        letter = offset + ord("A")
        num -= offset * (26**(3-i))
        mot += chr(letter)
    return [mot[:2], reste, mot[2:]]


x = input().split("-")
n = int(input())

p1, p2, p3 = x[0], int(x[1]), x[2]
a = str(p1)+str(p3)

position = convert(a, p2)
position += n
plate = convert_reverse(position)

print("-".join(plate))


