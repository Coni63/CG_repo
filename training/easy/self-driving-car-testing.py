import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
commands = input().split(";")
x, *commands = commands
commands = [(int(x[:-1]), x[-1]) for x in commands]

all_x = [int(x)-1]
for k, command in commands:
    for i in range(k):
        if command == "S":
            all_x += [all_x[-1]]
        if command == "L":
            all_x += [all_x[-1]-1]
        if command == "R":
            all_x += [all_x[-1]+1]

all_x = all_x[1:]

all_road = []
for i in range(n):
    k, *road = input().split(";")
    for j in range(int(k)):
        all_road.append(list(road[0]))

for road, car in zip(all_road, all_x):
    road[car] = "#"
    print("".join(road))
