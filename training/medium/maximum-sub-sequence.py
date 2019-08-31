import sys
import math
import bisect
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# def longest_increasing_subsequence(x):
#     """From Programmation Efficace - p57"""
#     n = len(x)
#     p = [None] * n
#     h = [None]
#     b = [float("-inf")]
#     for i in range(n):
#         if x[i] < b[-1]:
#             p[i] = h[-1]
#             h.append(i)
#             b.append(x[i])
#         else:
#             k = bisect.bisect_left(b, x[i])
#             h[k] = i
#             b[k] = x[i]
#             p[i] = h[k-i]
#     q = h[-1]
#     s = []
#     while q is not None:
#         s.append(x[q])
#         q = p[q]
#     return s[::-1]
    
def longest_increasing_subsequence(x):
    """Dynamic programming - O(n²)"""
    n = len(x)
    lis = [1 for x in range(n)]
    ant = {}
    for i in range(1, n):
        for j in range(i):
            if x[i] == x[j] + 1:
                if lis[j] + 1 > lis[i]:
                    lis[i] = lis[j] + 1
                    ant[i] = j
                    
    print(lis, file=sys.stderr)
    print(ant, file=sys.stderr)
    
    m = max(lis)
    sols = []
    for i, val in enumerate(lis):
        if val == m:
            path = [x[i]]
            idx = i
            for i in range(max(lis)-1):
                idx = ant[idx]
                path.append(x[idx])
            sols.append(path[::-1])
    
    valid_ans = sols[0]
    for sol in sols[1:]:
        if sol[0] < valid_ans[0]:
            valid_ans = sol
    return valid_ans

    
n = int(input())
l = [int(i) for i in input().split()]

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print(*longest_increasing_subsequence(l))
