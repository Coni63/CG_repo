import sys
import math
from itertools import groupby

message = input()
print("message : ", message, file=sys.stderr)

binary_code = "".join(format(ord(x), 'b').zfill(7) for x in message)
print("code : ", binary_code, file=sys.stderr)

res = []

for k, g in groupby(binary_code):
    if k == "0":
        res.append("00")
    else:
        res.append("0")
    res.append("0" * len(list(g)))   

print(" ".join(res))     
        
# To debug: print(mess, file=sys.stderr)