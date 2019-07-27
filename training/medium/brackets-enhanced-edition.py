import sys
import math
import re
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

opposite = {
            "{":"}", 
            "}":"{", 
            "[":"]", 
            "]":"[", 
            ">":"<", 
            "<":">", 
            "(":")", 
            ")":"("
            }

n = int(input())
for i in range(n):
    expression = input()
    regex = re.compile(r"[^<>\[\](){}]")
    exp = regex.sub("", expression)
    print(exp, file=sys.stderr)
    
    result = ""
    if len(exp) % 2 == 1:
        result  = "false"
    else:
        flag = True
        while flag:
            if len(exp) == 0:
                result = "true"
                flag = False
            else:
                flag = False
                result = "false"
                for i in range(len(exp)-1):
                    if exp[i] == opposite[exp[i+1]] or exp[i] == exp[i+1]:
                        exp = exp[:i] + exp[i+2:]
                        flag = True
                        print(exp, file=sys.stderr)  
                        break
            
    print(result)

    