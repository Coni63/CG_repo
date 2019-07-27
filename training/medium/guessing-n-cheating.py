import sys
import math

possible = [1 for _ in range(100)]

cheat = None
r = int(input())
for i in range(r):
    value, result = input().split(" ", 1)
    print(value, result, file=sys.stderr)
    value = int(value)-1
    
    if result == "too high":
        for j in range(value, 100):
            possible[j] = 0
        if sum(possible) == 0:
            cheat = i+1
            break
        
    elif result == "too low":
        for j in range(0, value+1):
            possible[j] = 0
        if sum(possible) == 0:
            cheat = i+1
            break
        
    elif result == "right on":
        if possible[value] == 0:
            cheat = i+1
            break
    
if cheat is None:
    print("No evidence of cheating")
else:
    print("Alice cheated in round {}".format(cheat))


