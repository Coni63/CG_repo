import sys
import math

# l : nb de place
# c : nb de rotation
# n : nb de groupe de x personnes
l, c, n = [int(i) for i in input().split()]

file = [int(input()) for _ in range(n)]
print(file, file=sys.stderr)
taille_file = sum(file)

if taille_file > l:
    packed = {}
    for i in range(n): #for each start
        ppl_in = 0
        index = 0
        while ppl_in + file[(i+index)%n] <= l:
            ppl_in += file[(i+index)%n]
            index += 1
        packed[i] = {"pers" : ppl_in , "next_index" : (i+index)%n}
    print(packed, file=sys.stderr)
    
    gain = 0
    start = 0
    for i in range(c):
        gain += packed[start]["pers"]
        start = packed[start]["next_index"]   
else:
    gain = c * taille_file
            
# To debug: print("Debug messages...", file=sys.stderr)
print(gain)
