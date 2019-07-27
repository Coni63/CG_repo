import sys
import math

n = int(input())
nums = [int(i) for i in input().split()]
nums.sort()

cost = 0
while len(nums) > 1:
    a, b, *nums = nums
    print(a, b, nums, file=sys.stderr)
    v = a+b
    cost += v
    nums.append(v)
    nums.sort()
print(cost)
