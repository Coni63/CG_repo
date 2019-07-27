import sys
import math
import string

def check10(x):
    if (x[:-1].isnumeric() == False) or (x[-1] not in "0123456789X"):
        return False
    
    s = 0
    for i in range(9):
        s += int(x[i]) * (10-i)
    rest = 11 - (s % 11)
    
    if rest == 10 and x[-1] == "X":
        return True
    elif x[-1].isnumeric():
        return (s + int(x[-1])) % 11 == 0
    else:
        return False

def check13(x):  
    if not x.isnumeric():
        return False
    
    a = [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3]
    s = 0
    for i in range(12):
        s += int(x[i]) * a[i]
    
    return (s + int(x[12])) % 10 == 0

    

wrong = []
n = int(input())
for i in range(n):
    isbn = input()
    if len(isbn) == 10:
        if not check10(isbn):
            wrong.append(isbn)
    elif len(isbn) == 13:
        if not check13(isbn):
            wrong.append(isbn)
    else:
        wrong.append(isbn)

print(str(len(wrong)) + " invalid:")
for each in wrong:
    print(each)
