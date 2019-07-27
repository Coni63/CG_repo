import sys
import math

class Gear:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
        self.rotation = None

inv = {"CW" : "CCW", "CCW" : "CW"}

n = int(input())
gears = [Gear(*[int(j) for j in input().split()]) for i in range(n)]
gears[0].rotation = "CW"

for i in range(10):
    for i, gear_a in enumerate(gears):
        for j, gear_b in enumerate(gears):
            if i != j:
                if [gear_a.rotation, gear_b.rotation].count(None) == 1:
                    diff = (gear_b.x - gear_a.x)**2 + (gear_b.y - gear_a.y)**2 - (gear_a.r + gear_b.r)**2
                    if diff == 0:
                        if gear_a.rotation is None:
                            gear_a.rotation = inv[gear_b.rotation]
                        else:
                            gear_b.rotation = inv[gear_a.rotation]
                        
    if gears[-1].rotation is not None:
        break

print(gears[-1].rotation if gears[-1].rotation is not None else "NOT MOVING")
