import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
height = 0

for level in range(1, 500):
    for offset in range(1, level+1):
        brick_required = (2*offset*level - offset*offset + offset)/2
        if brick_required == n:
            if offset > height:
                height = offset
                base = level
            print(level, offset, brick_required, file=sys.stderr)

print('base {} x height {}'.format(base, height), file=sys.stderr)

for step in range(height):
    print('*' * (base-height+step+1))

