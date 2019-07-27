import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

left = {"E":"N", "N":"W", "W":"S", "S":"E"}
right = {"E":"S", "S":"W", "W":"N", "N":"E"}

class Langton:
    def __init__(self):
        self.grid = []
        self.x = 0
        self.y = 0
        self.direction = "N"
        
    def update(self, X, Y, D):
        self.x = X
        self.y = Y
        self.direction = D
        
    def move(self):
        self.display()
        self.turn()
        self.toggle()
        self.avancer()
    
    def display(self):
        print("(%s, %s) - %s" % (self.x, self.y, self.direction), file=sys.stderr)
    
    def avancer(self):
        if self.direction == "N":
            self.y -= 1
        elif self.direction == "S":
            self.y += 1
        elif self.direction == "E":
            self.x += 1
        elif self.direction == "W":
            self.x -= 1
    
    def toggle(self):
        if self.grid[self.y][self.x] == ".":
            self.grid[self.y][self.x] = "#"
        else:
            self.grid[self.y][self.x] = "."
            
    def turn(self):
        if self.grid[self.y][self.x] == ".":
            self.direction = left[self.direction]
        elif self.grid[self.y][self.x] == "#":
            self.direction = right[self.direction]
    
fourmi = Langton()

w, h = [int(i) for i in input().split()]

x, y = [int(i) for i in input().split()]
d = input()
fourmi.update(x, y, d)

t = int(input())

for _ in range(h):
    c = input()
    fourmi.grid.append(list(c))

for _ in range(t):
    fourmi.move()
    
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
for i in range(h):
    print("".join(fourmi.grid[i]))
