import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

digit = []

test = [str(i) for i in range(10)]

n = int(input())
arr = input().split()
is_positive = ("-" not in arr)
with_decimal = ("." in arr)  
    
print("positive :", is_positive, file=sys.stderr)
print("decimal :", with_decimal, file=sys.stderr)

arr_2 = list(map(int,filter(lambda x: x in test, arr)))
print(arr_2, file=sys.stderr)

if is_positive:
    arr_2.sort(reverse = True)
    result = "".join(map(str, arr_2))
    print(result[:-1], file=sys.stderr)
    if with_decimal:
        result = result[:-1] + "." + result[-1]     
else:
    arr_2.sort(reverse = False)
    result = "-" + "".join(map(str, arr_2))
    print(result, file=sys.stderr)
    if with_decimal:
        result = result[:2] + "." + result[2:]
    
try:
    result = result.rstrip("0").rstrip(".")
except:
    pass

if result == "-0":
    print("0")
else:
    print(result)
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

