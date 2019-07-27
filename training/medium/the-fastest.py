import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

arr_full = []
arr_sec = []

n = int(input())
for i in range(n):
    t = input()
    arr_full.append(t)
    t_splitted = t.split(":")
    t_sec = int(t_splitted[0])*3600 + int(t_splitted[1])*60 + int(t_splitted[2])
    arr_sec.append(t_sec)
    
    time = arr_full[arr_sec.index(min(arr_sec))]

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print(time)
