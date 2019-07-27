import sys
import math
import numpy as np

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# with 
# a : rabbit
# b : chicken
# c : cow
# d :pegasi
# e : demons
# we have :
    
# a+b+c+d+e = heads
# 4a+2b+4c+4d+4e = legs
# 2a+2b+2c+2d+4e = eyes
# 2c+2e = horns
# 2d+2e = wings


dico = {}
animals = {'Cows':2, 'Pegasi':3, 'Demons':4, 'Chickens':1, 'Rabbits':0}
rev_animals = {val:key for key, val in animals.items()}

element = {'Eyes':2, 'Horns':3, 'Wings':4, 'Legs':1, 'Heads':0}
rev_element = {val:key for key, val in element.items()}

n = int(input())

species = input().split()
# print(species, file=sys.stderr)

for i in range(n):
    thing, number = input().split()
    dico[thing] = int(number)
#print(dico, file=sys.stderr)

#Mise en place du systeme d'equation
B = np.matrix([ dico.get("Heads", 0), dico.get("Legs", 0), dico.get("Eyes", 0), dico.get("Horns", 0), dico.get("Wings", 0) ], dtype=np.int16)
# print(B , file=sys.stderr)

A = np.matrix([ [1,1,1,1,1], [4,2,4,4,4], [2,2,2,2,4], [0,0,2,0,4], [0,2,0,2,2] ], dtype=np.int16)
# print(A , file=sys.stderr)

# Suppression des coloones ou l'animal n'est pas present
to_delete_col = [index for (animal, index) in animals.items() if animal not in species]
to_delete_col.sort(reverse = True)
#print(to_delete_col, file=sys.stderr)

kept_col = [x for x in range(5) if x not in to_delete_col]
kept_col.sort()
#print(kept_col, file=sys.stderr)

for index in to_delete_col:
    A = np.delete(A, index, 1)

#Suppresions des lignes ou on n'a pas d'element
to_delete_line = [value for elem, value in element.items() if elem not in dico.keys()]
to_delete_line.sort(reverse = True)

for index in to_delete_line:
    A = np.delete(A, index, 0)
    B = np.delete(B, index, 1)

#Systeme AX = B que l'on inverse
print(B, file=sys.stderr)
print(A, file=sys.stderr)

X = np.linalg.inv(A)*(B.T)
print(X , file=sys.stderr)

#recup des resultat avec assigment a l'elemn concerné
result = {}
for line, index in enumerate(kept_col): #le i-eme element de la matrice est le kept_col[i]-eme index a cause de la reduction de matrice
    a = rev_animals[index]
    b = int(X.item(line))
    result[a] = b

#affichage
for each in species:
    if result.get(each, None) is not None:
        print(each, result[each])


# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)


