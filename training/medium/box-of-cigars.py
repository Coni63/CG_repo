import sys
import math
from collections import Counter


# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
lgt = [int(input()) for _ in range(n)]
lgt.sort()

# print(lgt, file=sys.stderr)

# d = Counter()

# for i in range(1, n):
#     for j in range(i):
#         diff = lgt[i] - lgt[j]
#         d[diff] += 1

# print(d.most_common(3),file=sys.stderr)
# print(max(d.values()))

mini = min(lgt)
maxi = max(lgt)
diff = int(maxi-mini)
result = 0
for step in range(1, 30):
    for i in range(n):
        cnt = 1
        first = lgt[i]
        current = lgt[i]
        while current < maxi:
            current += step
            if current in lgt:
                cnt += 1
            else:
                break
        result = max(cnt, result)
print(result)
