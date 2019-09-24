import sys
import math
import time

class Point:
    def __init__(self, x, y, index):
        self.x = x
        self.y = y
        self.n = 0
        self.pivot = False
        self.index = index

    def __repr__(self):
        return f"Pts({self.x}, {self.y}) = {self.n}"

    def set_pivot(self):
        for pts in listed_points:
            pts.pivot = False
        self.pivot = True
        self.n += 1
        
class Vector:
    def __init__(self, dx, dy):
        self.x = dx
        self.y = dy
        
    def sqnorm(self):
        return self.x**2 + self.y**2
        
    def norm(self):
        return math.sqrt(self.sqnorm())
        
    def dot(self, other):
        return self.x*other.x + self.y*other.y

    def norm_dot(self, other):
        return self.dot(other)/(self.norm()*other.norm())

    def cross(self, other):
        return self.x*other.y - self.y*other.x
    
    def norm_cross(self, other):
        return self.cross(other)/(self.norm()*other.norm())
        
    def isClockwise(self, other):
        return self.cross(other) > 0
        
    def __mul__(self, a):
        self.x *= a
        self.y *= a
        
    def copy(self):
        return Vector(self.x, self.y)

k = int(input())
n = int(input())
pivot_number = int(input())
listed_points = []
for i in range(k):
    x, y = [int(j) for j in input().split()]
    listed_points.append(Point(x, y, i))

tic = time.time()

alpha = 0                                # angle of the line "l"

prev_pivot = listed_points[pivot_number] # require to save the previous pivot to not select it again after a change
pivot = listed_points[pivot_number]
pivot.set_pivot()
line = Vector(1, 0)

memo = []                                # stores (previous_pivot, pivot, rotation) which is required for memoization
skip_memo = True                        # once we use the memo, we should not go thru it for the last remaining steps

loop = 1
while loop <= n:
    closest_pts = None
    mini_dot = 1e10
    for pts in listed_points:
        if not pts.pivot and pts != prev_pivot:
            v = Vector(pts.x-pivot.x, pts.y-pivot.y)
            if not line.isClockwise(v):  v * -1  # invert the vector to have the angle from the left
            dotv = line.dot(v) / v.norm()        # no need to normalize "line" as we just compare
            if dotv < mini_dot:
                mini_dot = dotv
                possible_pivot = pts
                possible_line = v
    
    loop += 1
    line = possible_line
    prev_pivot, pivot = pivot, possible_pivot                  # swap pivots
    pivot.set_pivot()
    
    # memoization
    if not (prev_pivot, pivot) in memo:
        memo.append((prev_pivot, pivot))
    elif not skip_memo:
        prev_index = memo.index((prev_pivot, pivot))
        loop_freq = loop - prev_index - 2    # -2 is because the loops starts at 1, and the index at 0
        remaining_steps = n - loop
        turn = remaining_steps // loop_freq
        n = loop + (remaining_steps % loop_freq)
        for pprivot, cpivot in memo[prev_index:]:  # increase each points by the number of loops skipped with memoization
            cpivot.n += turn
        skip_memo = True

toc = time.time()
print(toc-tic, file=sys.stderr)

print(pivot.index)
for pts in listed_points:
    print(pts.n)
