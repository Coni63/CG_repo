import sys
import math
import re

split_string = lambda x, n : [x[i:i+n] for i in range(0, len(x), n)]

def check_valid(code):
    p = re.compile('^[0| ]+$')
    if p.match(code):
        print("regex OK", file=sys.stderr)
    else:
        return False
        
    code = code.split()
    if len(code) % 2 == 0:
        print("len OK", file=sys.stderr)
    else:
        return False
    
    current_state = code[0]
    for i in range(2, len(code)-1, 2):
        if (current_state == "0" and code[i] == "00") or (current_state == "00" and code[i] == "0"):
            current_state = code[i]
        else:
            return False
    print("alternance OK", file=sys.stderr)
    
    S = sum(len(code[i]) for i in range(len(code)) if i%2 == 1)
    if S % 7 == 0:
        print("taille OK", file=sys.stderr)
    else:
        return False
    
    return True
    

encrypt = input()
print(encrypt, file=sys.stderr)

if check_valid(encrypt):
    print("VALID", file=sys.stderr)
    encrypt = encrypt.split()
    binary = ""
    for i in range (0, len(encrypt), 2):
        key = encrypt[i]
        repeat = len( encrypt[i+1] )
        if key == "0":
            binary += "1"*repeat
        else:
            binary += "0"*repeat

    split_binary = split_string(binary,7)
    ascii = [chr(int(x, 2)) for x in split_binary]
    print(''.join(ascii))

else:
    print("INVALID")
