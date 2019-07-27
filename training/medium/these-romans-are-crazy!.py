import sys
import math
from itertools import groupby

tableau = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
valeur = [1000,900,500,400,100,90,50,40,10,9,5,4,1]

R_to_D = dict(zip(tableau, valeur))
D_to_R = zip(valeur, tableau)

print(R_to_D, file = sys.stderr)
print(D_to_R, file = sys.stderr)

def convert_R_to_D(n):
    total = []
    for letter, group in groupby(n):
        occurence =  len(list(group))
        #print("letter %s appears %s times"%(letter, occurence) ,file=sys.stderr)
        value = R_to_D[letter] * occurence
        total.append(value)
    print(total, file = sys.stderr)
    
    decimal = total[0]    
    for i in range(len(total)-1):
        if total[i+1] < total[i]:
            decimal += total[i+1]
        elif total[i+1] > total[i]:
            decimal += total[i+1]-2*total[i]  # 2 x previous value to remove to previous addition and then do the substract   
    print(decimal, file = sys.stderr)
    
    return decimal

def convert_D_to_R(n):
    result = []
    for val, letter in D_to_R:
        while n >= val:
            result.append(letter)
            n -= val
    return ''.join(result)

    
    
    


# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

rom_1 = input()
rom_2 = input()

print("Objectif : %s + %s" % (rom_1, rom_2) ,file=sys.stderr)

num_1 = convert_R_to_D(rom_1)
num_2 = convert_R_to_D(rom_2)

result = convert_D_to_R( num_1 + num_2 )

print(result)