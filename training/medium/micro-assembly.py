import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

a, b, c, d = [int(i) for i in input().split()]
list_instruction = []
n = int(input())
for i in range(n):
    instruction = input().split()
    list_instruction.append(instruction)

index = 0
while index <= n-1:
    instruction = list_instruction[index]
    if instruction[0] == "MOV":
        exec(instruction[1] + "=" + instruction[2])
        index += 1
    elif instruction[0] == "ADD":
        exec(instruction[1] + "=" + instruction[2] + "+" + instruction[3])
        index += 1
    elif instruction[0] == "SUB":
        exec(instruction[1] + "=" + instruction[2] + "-" + instruction[3])
        index += 1
    else:
        if eval(instruction[2] + "!=" + instruction[3]):
            index = int(instruction[1])
        else:
            index += 1
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print(a, b, c, d)
