import sys
import math

digit = {
        "0" : [True, True, True, False, True, True, True],
        "1" : [False, False, True, False, False, True, False],
        "2" : [True, False, True, True, True, False, True],
        "3" : [True, False, True, True, False, True, True],
        "4" : [False, True, True, True, False, True, False],
        "5" : [True, True, False, True, False, True, True],
        "6" : [True, True, False, True, True, True, True],
        "7" : [True, False, True, False, False, True, False],
        "8" : [True, True, True, True, True, True, True],
        "9" : [True, True, True, True, False, True, True],
        }

n = int(input())
c = input()
s = int(input())

for line in range(2*s+3):
    result = []
    for each in str(n):
        if line == 0: # barres horizontales sup
            if digit[each][0] == True:
                result.append(" " + s*c + " ")
            else:
                result.append((s+2)*" ")
        elif line == s+1: # barres horizontales mid
            if digit[each][3] == True:
                result.append(" " + s*c + " ")
            else:
                result.append((s+2)*" ")
        elif line == 2*(s+1): # barres horizontales bottom
            if digit[each][6] == True:
                result.append(" " + s*c + " ")
            else:
                result.append((s+2)*" ")
        elif 0 < line < s+1: #barres vert top
            if digit[each][1] == True and digit[each][2] == True:
                result.append(c + s*" " + c)
            elif digit[each][1] == True and digit[each][2] == False:
                result.append(c + s*" " + " ")
            elif digit[each][1] == False and digit[each][2] == True:
                result.append(" " + s*" " + c)
        elif s+1 < line < 2*(s+1): #barre vert bottom
            if digit[each][4] == True and digit[each][5] == True:
                result.append(c + s*" " + c)
            elif digit[each][4] == True and digit[each][5] == False:
                result.append(c + s*" " + " ")
            elif digit[each][4] == False and digit[each][5] == True:
                result.append(" " + s*" " + c)
    print(" ".join(result).rstrip())
        
            



# To debug: print("Debug messages...", file=sys.stderr)


