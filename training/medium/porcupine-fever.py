import sys
import math

class Cage:
    def __init__(self, s, h, a):
        self.sick = s
        self.healthy = h
        self.alive = a
        
    def evolve(self):
        self.alive -= self.sick
        self.sick = min(self.sick*2, self.healthy)
        self.healthy -= self.sick

instances = []

n = int(input())
y = int(input())
for i in range(n):
    s, h, a = [int(j) for j in input().split()]
    instances.append(Cage(s, h, a))
   
for i in range(y):
    for c in instances:
        c.evolve()
    r = sum(x.alive for x in instances)
    print(r)
    if r == 0:
        break
        
