import sys
import math

n, k = [int(i) for i in input().split()]

limit = min(n, k)
final = []
queue = [[x+1] for x in range(0, limit)]

print(queue, file=sys.stderr)

while len(queue) > 0:
    elem = queue.pop(0)
    remaining = n - sum(elem)
    if remaining == 0:
        final.append(elem)
    else:
        for i in range(1, min(remaining, k)+1):
            new_state = elem+[i]
            queue.append(new_state)

str_result = [" ".join([str(y) for y in x]) for x in final]
str_result.sort()
print("\n".join(str_result))
