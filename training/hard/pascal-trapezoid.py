import sys
import math

def next_line(starting_line, reverse = False):
    output = []
    for i in range(elem_number):
        if i == 0:
            output.append(starting_line[i])
        elif i == len(starting_line):
            output.append(starting_line[i-1])
        else:
            first = str(starting_line[i-1])
            second = str(starting_line[i])
            if first.isnumeric() and second.isnumeric():
                out = int(first) + int(second)
            else:
                if reverse:
                    out = second + first
                else:
                    out = first + second
            output.append(out)
    return output


start_lvl, end_lvl, elem_number = [int(i) for i in input().split()]
start_line = input().split()

if elem_number == 0:
    print(start_line[0])
elif elem_number == end_lvl + start_lvl - 1:
    print(start_line[-1])
else:
    if elem_number < (end_lvl + start_lvl) // 2: # si coté gauche
        result = start_line
        reverse = False
    else:
        result = start_line[::-1]
        elem_number = start_lvl + end_lvl - elem_number
        reverse = True
        
    for _ in range(end_lvl-1):
        result = next_line(result, reverse)
    print(result[elem_number-1])


# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)


