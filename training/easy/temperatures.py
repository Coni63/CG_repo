import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # the number of temperatures to analyse
temps = input()  # the n temperatures expressed as integers ranging from -273 to 5526

closest=5526

if len(temps)>0:
    temps = temps.split(" ")
    for i in temps:
        current = int(i)
        if abs(current) < abs(closest):
            closest = current
        if abs(current)==abs(closest):
            closest = max(current,closest)
    
    print(closest) 
else:
    print("0")


