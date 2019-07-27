import sys
import math


class Point:
    def __init__(self, X, Y):
        self.x = X
        self.y = Y
        
        
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
class Thor:
    def __init__(self, X, Y):
        self.x = X
        self.y = Y
        self.remaining_strikes = 0
        self.FOV = 4
        
    def goto(self, target):
        direction = ""
        dx = target.x - self.x
        dy = target.y - self.y
        if dy > 0:
            direction += "S"
            self.y += 1
        elif dy < 0:
            direction += "N"
            self.y -= 1
        if dx > 0:
            direction += "E"
            self.x += 1
        elif dx < 0:
            direction += "W"
            self.x -= 1
        if direction == "":
            self.wait()
        else:
            print(direction)
        
    def wait(self):
        print("WAIT")
    
    def strike(self):
        print("STRIKE")
    
            
class Giant:
    instances = []
    def __init__(self, X, Y):
        self.x = X
        self.y = Y
        self.distance = 0
        self.instances.append(self)
        
    def in_area(self, hero):
        return abs(self.x - hero.x) <= 4 and abs(self.y - hero.y) <= 4
        
    def distance_to(self, hero):
        self.distance = abs(self.x - hero.x) + abs(self.y - hero.y)
        
    
tx, ty = [int(i) for i in input().split()]
Moi = Thor(tx, ty)

while True:
    # h: the remaining number of hammer strikes.
    # n: the number of giants which are still present on the map.
    h, n = [int(i) for i in input().split()]
    Moi.remaining_strikes = h
    Giant.instances = []
    for i in range(n):
        x, y = [int(j) for j in input().split()]
        print(x, y, file=sys.stderr)
        Giant(x, y)

    for G in Giant.instances:
        G.distance_to(Moi)
        
    close_count = sum(1 for g in Giant.instances if g.distance < 5 )
    print(close_count, file=sys.stderr)
    closest_giant = min(Giant.instances, key = lambda x: x.distance )
    if closest_giant.in_area(Moi) and (close_count >= 2 or close_count == n):
        Moi.strike()
    else:
        middle_x = sum(g.x for g in Giant.instances)//len(Giant.instances)
        middle_y = sum(g.y for g in Giant.instances)//len(Giant.instances)
        Moi.goto(Point(middle_x, middle_y))
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)


    # The movement or action to be carried out: WAIT STRIKE N NE E SE S SW W or N
    #print("STRIKE")
