import sys
import math


def andrew(S):
    S.sort()
    top = []
    bot = []
    for p in S:
        while len(top) >=2 and not left_turn(p, top[-1], top[-2]):
            top.pop()
        top.append(p)
        while len(bot) >=2 and not left_turn(bot[-2], bot[-1], p):
            bot.pop()
        bot.append(p)
    return bot[:-1] + top[:0:-1]
        

def left_turn(a, b, c):
    return (a[0]-c[0])*(b[1]-c[1]) - (a[1]-c[1])*(b[0]-c[0]) > 0
    
    
n = int(input())

pts = []
for i in range(n):
    x, y = [int(j) for j in input().split()]
    pts.append((x, y))

ext_shape = andrew(pts)
print(ext_shape, file=sys.stderr)

s = len(ext_shape)

dist = 0
for i in range(s):
    a = ext_shape[i]
    b = ext_shape[(i+1)%s]
    dist += math.sqrt((b[0]-a[0])**2 + (b[1]-a[1])**2)


dist += (2*math.pi * 3) # offset de 3 m


print( math.ceil(dist/5) )
