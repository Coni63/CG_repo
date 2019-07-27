import sys
import math
import itertools

def add(x, y):
    return True, x+y
    # if x+y > 999:
    #     return False, 0
    # else:
    #     return True, x+y

def sub(x, y):
    v = max(x, y) - min(x, y)
    if v != 0:
        return True, v
    else:
        return False, 0
    # if v > 999 or v == 0:
    #     return False, 0
    # else:
    #     return True, v

def mult(x, y):
    v = x*y
    if x > 1 and y > 1:
        return True, v
    else:
        return False, 0
    # if v > 999 or x == 1 or y == 1:
    #     return False, 0
    # else:
    #     return True, v

def div(x, y):
    a = max(x, y)
    b = min(x, y)
    if b >= 2 and a % b == 0:
        return True, a // b
    else:
        return False, 0

#### V1
# def bfs(queue):
#     diff = 999
#     while len(queue) > 0:
#         num = queue.pop(0)
#         for pair in itertools.combinations(num, r=2):
#             remaining = num.copy()
#             remaining.remove(pair[0])
#             remaining.remove(pair[1])
#             for op in ops:
#                 valid, val = op(*pair)
#                 if valid:
#                     diff = min(abs(result - val) , diff)
                        
#                     if val == result:
#                         return "POSSIBLE", 6-len(remaining)-1
#                     else:
#                         if len(remaining) >= 1:
#                             next_one = sorted(remaining + [val])
#                             if next_one not in queue:
#                                 queue.append(next_one)
#     return "IMPOSSIBLE", diff

#### V2
# def bfs(queue):
#     diff = 999
#     while len(queue) > 0:
#         num = queue.pop(0)
#         k = len(num)
#         remaining = num.copy()
#         for i in range(k):
#             for j in range(i+1, k):
#                 remaining = num.copy()
#                 pair= (remaining[i], remaining[j])
#                 del remaining[i]
#                 del remaining[j-1]
#                 for op in ops:
#                     valid, val = op(*pair)
#                     if valid:
#                         diff = min(abs(result - val) , diff)
                            
#                         if val == result:
#                             return "POSSIBLE", 6-len(remaining)-1
#                         else:
#                             if len(remaining) >= 1:
#                                 next_one = sorted(remaining + [val])
#                                 if next_one not in queue:
#                                     queue.append(next_one)
#     return "IMPOSSIBLE", diff
    
def search(numbers, target, depth):
    n = len(numbers)
    
    if target in numbers:
        return "POSSIBLE", depth
    
    if n == 1:
        return "IMPOSSIBLE", abs(numbers[0] - target)
    
    for numa in range(n):
        for numb in range(numa+1, n):
            print(n, numb, numa, numbers, file=sys.stderr)
            numbers.pop(numb)
            numbers.pop(numa)
            
            valid, value = add(numa, numb)
            if valid: 
                return search(numbers + [value], target, depth + 1)
            
            valid, value = sub(numa, numb)
            if valid: 
                return search(numbers + [value], target, depth + 1)
            
            valid, value = mult(numa, numb)
            if valid: 
                return search(numbers + [value], target, depth + 1)
            
            valid, value = div(numa, numb)
            if valid: 
                return search(numbers + [value], target, depth + 1)

ops = [add, sub, mult, div]
result = int(input())
nums = sorted([int(i) for i in input().split()])

a, b = search(nums, result, 0)

# queue = [nums]
# a, b = bfs(queue)
print(a)
print(b)
