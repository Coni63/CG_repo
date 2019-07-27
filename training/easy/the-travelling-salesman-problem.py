import sys
import math

class city:
    def __init__(self, i, x, y):
        self.ID = i
        self.x = x
        self.y = y
        
    def dist_to(self, other):
        return math.sqrt( (self.x-other.x)**2 + (self.y-other.y)**2 )


# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
path = []
cities = []
total_d = 0


n = int(input())
for i in range(n):
    x, y = [int(j) for j in input().split()]
    cities.append(city(i, x, y))

path.append(cities[0])

for i in range(n-1):
    current_city = path[-1]
    print(current_city.ID, file=sys.stderr)
    shortest_d = 1e8
    for cty in cities:
        if cty not in path:
            d = current_city.dist_to(cty)
            if d < shortest_d:
                candidate = cty
                shortest_d = d
    path.append(candidate)
    total_d += shortest_d

total_d += path[-1].dist_to(path[0])

print(round(total_d))
    
