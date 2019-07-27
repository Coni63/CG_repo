import sys
import math

arr = []
l = 0

count = int(input())

for i in range(count):
    line = input().split('.')
    level = len(line)-1
    nom = line[-1]
    if level == 0:
        arr.append([nom])
    elif level <= l:
        origin = arr[-1][:level]
        arr.append(origin + [nom])
    elif level == l+1:
        arr[-1] = arr[-1] + [nom]
    l = level    

for each in arr:
    print(" > ".join(each))
