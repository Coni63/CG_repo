import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

frog_number = int(input())
frogs_distance = [float(x) for x in input().split()]
initial_position_x, initial_position_y = [float(x) for x in input().split()]
mass = int(input())
alpha = int(input())
speed = float(input())
a, b = [float(x) for x in input().split()]  # gravity

speed_x = math.cos(alpha*math.pi / 180) * speed
speed_y = math.sin(alpha*math.pi / 180) * speed

delta = speed_y**2 - 2*b*initial_position_y
time = (-speed_y-math.sqrt(delta))/b

final = round(a*time**2/2 + speed_x*time + initial_position_x, 2)

print(sum(1 if x > final else 0 for x in frogs_distance)+1)
