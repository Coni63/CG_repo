import sys
from itertools import groupby

def conway(suite):
    next_terme = []
    for k, g in groupby(suite):
        next_terme.append(str(len(list(g))))
        next_terme.append(k)
    return next_terme
    

r = int(input()) # initial number
l = int(input()) # number of step

terme = [str(r)]
freq = []
key = []

for i in range(1, l):
    terme = conway(terme)
    print(i, terme, file=sys.stderr)

print(' '.join(terme))
# To debug: print("Debug messages...", file=sys.stderr)
   
