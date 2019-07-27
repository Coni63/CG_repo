import sys
import math



def isvalid(card):
    # step 1
    every_2_digit = [2*x if x < 5 else 2*x-9 for x in card[::2]]
    
    # step 2
    s1 = sum(every_2_digit)
    
    # step 3
    s2 = sum(card[1::2])
    
    # step 4
    s = s1 + s2
    
    # step 5
    return s%10 == 0


n = int(input())
for i in range(n):
    card = list(map(int, list(input().replace(" ", ""))))
    ans = isvalid(card)
    print("YES" if ans else "NO")
