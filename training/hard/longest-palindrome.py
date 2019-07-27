import sys
import math
import time

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def manacher(text):
    if s == "":
        return (0, 1)
    t = "^#" + "#".join(s) + "#$"
    c = 0
    d = 0
    p = [0] * len(t)
    
    for i in range(1, len(t)-1):
        mirror = 2 * c - i
        p[i] = max(0, min(d-i, p[mirror]))
        while t[i+1+p[i]] == t[i-1-p[i]]:
            p[i] += 1
        if i + p[i] > d:
            c = i
            d = i + p[i]
    
    longest_palindrome = max(p[i] for i in range(1, len(t)-1))
    result = []
    for i in range(1, len(t)-1):
        if p[i] == longest_palindrome:
            result.append( ((i-p[i])//2, (i+p[i])//2) )
    return result
    
s = input()

print("length : {} chars".format(len(s)), file=sys.stderr)

debut = time.time()

arr_result = manacher(s)

duration = time.time() - debut
print("{} s".format(duration), file=sys.stderr)

for res in arr_result:
    print(s[res[0]:res[1]])