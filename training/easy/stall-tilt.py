import sys
import math

letter = "abcdefghijklmnopqrstuvwxyz"
angle_max = math.radians(60)
g = 9.81

class Moto:
    def __init__(self, letter, speed):
        self.name=letter
        self.speed = speed
        self.falls = 1e6
        
    def drive(self, bends):
        for i, bend in enumerate(bends):
            if math.atan(self.speed**2 / (bend * g)) > angle_max:
                self.falls = i+1
                break
        
    def __repr__(self):
        return "{} - {} m/s - falls @{}".format(self.name, self.speed, self.falls)

motos = []

n = int(input())
v = int(input())
for i in range(n):
    speed = int(input())
    motos.append(Moto(letter[i], speed))

bends = [int(input()) for i in range(v)]

vmax = int(math.sqrt(math.tan(angle_max)*min(bends)*g))
print(vmax)
print("y")

for each in motos:
    each.drive(bends)
    
motos.sort(key = lambda x: (x.falls, x.speed), reverse=True)
for each in motos:
    print(each.name)
