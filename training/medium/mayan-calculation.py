import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def numberToBase(n, b):
    power=int(math.log(n,b))
    number = []
    while power >= 0:
        temp = int(n/(b**power))
        number.append(temp)
        n -= temp*(b**power)
        power -= 1
        
    return number

def split_by_n( seq, n ):
    """A generator to divide a sequence into chunks of n units."""
    while seq:
        yield seq[:n]
        seq = seq[n:]
        
def fill_list(arr):
    for i in range(20):
        temp = []
        for j in range(h):
            temp.append(arr[j][i])
        
        list_int_maya[i]=[temp] 
        
def maya_to_int(arr, liste):
    for i in range(20):
        if liste[i] == arr:
            return i

########################
###Declaration digits###
########################

l, h = [int(i) for i in input().split()]

##############################
###Determination caracteres###
##############################
res = []
for i in range(h):
    numeral = input()
    res.append(list(split_by_n(numeral,l)))


list_int_maya = {}
fill_list(res)

#test = list_int_maya[0]
#a = maya_to_int(test, list_int_maya)

##############################
### Determination nombre 1 ###
##############################

s1 = int(input())
digit1 = int(s1/h)

inp_1 = [[] for i in range(digit1)]
inp_int_1 = []

#recup du caractere
for i in range(s1):
    num_1line = input()
    nth = int(i/h)
    inp_1[nth].append(num_1line)

#mise en tableau de int
for each in inp_1:
    inp_int_1.append(maya_to_int([each], list_int_maya))
    
print(inp_int_1, file=sys.stderr)

#determination du nombre en base 20
num1 = 0
for i in range(len(inp_int_1)):
    num1 += inp_int_1[i]*(20**(len(inp_int_1)-i-1))
    
print(num1, file=sys.stderr)

print("*********", file=sys.stderr)  

##############################
### Determination nombre 2 ###
##############################

s2 = int(input())
digit2 = int(s2/h)

inp_2 = [[] for i in range(digit2)]
inp_int_2 = []

#recup du caractere
for i in range(s2):
    num_2line = input()
    nth = int(i/h)
    inp_2[nth].append(num_2line)

#mise en tableau de int 
for each in inp_2:
    inp_int_2.append(maya_to_int([each], list_int_maya)) 
    
print(inp_int_2, file=sys.stderr)

#determination du nombre en base 20
num2 = 0
for i in range(len(inp_int_2)):
    num2 += inp_int_2[i]*(20**(len(inp_int_2)-i-1)  )
    
print(num2, file=sys.stderr)

print("*********", file=sys.stderr)  

###############################
### Determination operation ###
###############################

operation = input()

print(operation, file=sys.stderr)

if operation== "+":
    tot = num1 + num2
elif operation== "-":
    tot = num1 - num2
elif operation== "/" and num2 != 0:
    tot = num1 / num2
else:
    tot = num1 * num2
    
print(tot, file=sys.stderr)
if tot != 0:
    tot2 = numberToBase(tot,20)
else:
    tot2 = [0]

print(tot2, file=sys.stderr)

print("*********", file=sys.stderr)  

for each in tot2:
    for i in range(h):
        print(list_int_maya[each][0][i])

# To debug: print("Debug messages...", file=sys.stderr)
