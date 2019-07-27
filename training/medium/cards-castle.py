import sys
import math

arr = []

def check_stability_per_line(line):
    for x in range(w-1):
        if arr[line][x] == '/' and arr[line][x+1] != "\\":
            return "unstable"
    for x in reversed(range(1, w)):
        if arr[line][x] == "\\" and arr[line][x-1] != "/":
            return "unstable"
    for x in range(1, w):
        if arr[line][x] == '\\' and arr[line][x-1] != "/":
            return "unstable"
    #for x in range(w-1):
    #    if arr[line][x] == '/' and arr[line][x+1] != "\\":
    #        return "unstable"
    return "stable"

def check_support(line):
    for x in range(w):
        if arr[line][x] == "\\":
            if arr[line+1][x] != "/":
                return "unstable"
        elif arr[line][x] == "/":
            if arr[line+1][x] != "\\":
                return "unstable"
    return "stable"
    
    
h = int(input())
w = 0

for i in range(h):
    row = input()
    arr.append(row)
    w = len(row)
    print(row, file=sys.stderr)

print("", file=sys.stderr)

flag = True

if flag:
    for y in reversed(range(h)):
        print("%s => %s" % (arr[y] , check_stability_per_line(y)), file=sys.stderr)
        if check_stability_per_line(y) == "unstable":
            flag = False

if flag:
    for y in range(h-1):
        if check_support(y) == "unstable":
            flag = False

if flag:
    print("STABLE")
else:
    print("UNSTABLE")
    
