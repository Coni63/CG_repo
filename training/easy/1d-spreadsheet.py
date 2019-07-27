import sys
import math

def process_args(x):
    if x.startswith("$"):
        idx = int(x[1:])
        try:
            return sheet[idx]
        except:
            return "#REF"
    elif x == "#REF":
        return x
    elif x == "_":
        return x
    else:
        return int(x)

def set_value(a, b, idx=None):
    return a
    
def add(a, b, idx=None):
    return a+b
    
def sub(a, b, idx=None):
    return a-b
    
def mult(a, b, idx=None):
    return a*b
    
    
mapper = {"VALUE" : set_value, "ADD" : add, "SUB" : sub, "MULT" : mult}


n = int(input())
sheet = ["#REF"] * n
ops = []

for i in range(n):
    operation, arg_1, arg_2 = input().split()
    ops.append((i, operation, arg_1, arg_2))

while len(ops) > 0:
    idx, operation, x1, x2 = ops.pop(0)
    a = process_args(x1)
    b = process_args(x2)
    if a != "#REF" and b != "#REF":
        sheet[idx] = mapper[operation](a, b, idx)
    else:
        ops.append((idx, operation, x1, x2))

for each in sheet:
    print(each)
