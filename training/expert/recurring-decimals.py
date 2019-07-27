import sys
import math

#http://eli.thegreenplace.net/2009/02/25/project-euler-problem-26/

def cycle_length(num):
    reste = 10
    i = 0
    #Calcul des décimales tant que le reste n'est pas égal à 10
    while reste != 10 or i < 1:
        reste = (reste % num) * 10
        i += 1
    return i

n = int(input())

if n%2!=0 and n%5!=0 :
    length = cycle_length(n)
    result = "{0:.{size}f}".format(1/n, size = length)
    result = result.split('.')
    final = result[0]+".("+result[1]+")"
    print(final)
else:
    result = "{0:.15f}".format(1/n).rstrip('0')
    print(result)

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

