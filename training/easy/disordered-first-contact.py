import sys
import math

def getPieceEncode(x):
    i = 1
    while len(x) > 0:
        c = x[:i]
        x = x[i:]
        i += 1
        yield c
        
def getPieceDecode(x, chunk):
    for idx, l in enumerate(chunk):
        if (len(chunk)-idx) % 2 == 0:
            c = x[:l]
            x = x[l:]
        else:
            c = x[-l:]
            x = x[:-l]
        yield c
        
def encode(x):
    new_msg = ""
    for i, code in enumerate(getPieceEncode(x)):
        if i % 2 == 1:
            new_msg = code + new_msg
        else:
            new_msg = new_msg + code
    return new_msg

def getNumberPieces(x):
    i = 1
    s = 1
    l = [1]
    while len(x) > s:
        i += 1
        s += i
        l.append(min(i, i+len(x)-s))
    return l[::-1]

def decode(x):
    new_msg = ""
    n = getNumberPieces(x)
    for i, code in enumerate(getPieceDecode(x, n)):
        new_msg = code + new_msg
    return new_msg
    

n = int(input())
message = input()

if n < 0:
    for i in range(-n):
        message = encode(message)
else:
    for i in range(n):
        message = decode(message)

print(message)
