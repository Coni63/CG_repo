import sys
import math

def pgcd(a,b) :  
   while a%b != 0 : 
      a, b = b, a%b 
   return b

n = int(input())
for i in range(n):
    x, y = input().split("/")
    is_negative = int(x)*int(y)<0
    x, y = abs(int(x)), abs(int(y))
    
    if y == 0:
        print("DIVISION BY ZERO")
    elif x == 0:
        print(0)
    else:
        a = int(x/y)
        b = x-a*y
        c = pgcd(b,y)
        if a == 0:
            if is_negative:
                print("-%d/%d" %(b/c,y/c))
            else:
                print("%d/%d" %(b/c,y/c))
        elif b == 0:
            if is_negative:
                print(-a)
            else:
                print(a)
        else:
            if is_negative:
                print("-%s %d/%d" %(a,b/c,y/c))
            else:
                print("%s %d/%d" %(a,b/c,y/c))
            


    # To debug: print("Debug messages...", file=sys.stderr)

