import sys
import math

class Apple:
    def __init__(self, i, x, y, z, r):
        self.ID = i
        self.x = x
        self.y = y
        self.z = z
        self.r = r
        self.xmin = self.x - r
        self.xmax = self.x + r
        self.falling = False
        
    def hit(self, other):
        d = math.sqrt( (self.x-other.x)**2 + (self.y-other.y)**2 )
        if d < self.r + other.r:
            return True
        else:
            return False
        
# initial state
apples = []

n, index = [int(i) for i in input().split()]
for i in range(n):
    x, y, z, r = [int(j) for j in input().split()]
    apples.append(Apple(i, x, y, z, r))

apples[index].falling = True
current_xmin = apples[index].xmin
current_xmax = apples[index].xmax

# computation
apples.sort(key = lambda a:a.z, reverse=True)

for i, appl in enumerate(apples):
    if appl.falling:
        for other_appl in apples[i+1:]:
            if appl.hit(other_appl):
                other_appl.falling = True
        
print(len(list(filter(lambda k:k.falling == False, apples))))
