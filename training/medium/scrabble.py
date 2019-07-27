import sys
import math
import operator

def points(mot):
    return sum(score[lettre] for lettre in mot)
    
def decomposer(mot):
    dictionnaire = {}
    for each_char in set(mot):
        dictionnaire[each_char] = mot.count(each_char)
    return dictionnaire

score = {   "a":1, "b":3, "c":3, "d":2, "e":1, "f":4, 
            "g":2, "h":4, "i":1, "j":8, "k":5, "l":1,
            "m":3, "n":1, "o":1, "p":3, "q":10, "r":1, 
            "s":1, "t":1, "u":1, "v":4, "w":4, "x":8, 
            "y":4, "z":10
        }

freq_word = {}
possible_word = []
best_score = 0

n = int(input())
dico = [(n-i, input()) for i in range(n)] #position inverted (for the sorting at the end) and word

letters = input()
freq_word[letters] = decomposer(letters) 
        
for each_word in dico: 
    flag = True
    freq_word[each_word[1]] = decomposer(each_word[1])
    for each in freq_word[each_word[1]]:
        if (each not in freq_word[letters].keys() or freq_word[each_word[1]][each] > freq_word[letters][each]) and (flag):  #si on a pas assez de fois cette lettre ou qu'on ne l'a pas du tout
            flag = False
            
    if flag == True:
        possible_word.append((each_word[1], each_word[0], points(each_word[1])))
 
possible_word.sort(key = lambda l: (l[2], l[1]), reverse=True)
print(possible_word, file=sys.stderr) 

print(possible_word[0][0])

# To debug: print("Debug messages...", file=sys.stderr)




