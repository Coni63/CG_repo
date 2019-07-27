import sys
import math

nom = {}
votant = []

c = int(input())
for i in range(c):
    name = input()
    nom[i+1] = name
    
print(nom, file=sys.stderr)   

v = int(input())
for i in range(v):
    votes = input()
    print(votes, file=sys.stderr)
    votant.append(votes.split(" "))
    

while len(nom.keys())>1:
    print(votant, file=sys.stderr)
    result = {}
    
    for each in nom.keys():
        result[each]=0
    
    for each_votant in votant:
        result[int(each_votant[0])]+=1
    
    print(result, file=sys.stderr)
    
    min_voix = 1000
    id_min = 0
    
    for each_candidat in result:
        if result[each_candidat]<min_voix or (result[each_candidat]==min_voix and each_candidat<id_min):
            min_voix = result[each_candidat]
            id_min = each_candidat
    
    print(str(id_min)+" est eliminé - "+nom[id_min], file=sys.stderr)
    print(nom[id_min])
    
    del nom[id_min]
    
    for each_votant in votant:
        each_votant.remove(str(id_min))
    
    
print("winner:"+nom[list(nom.keys())[0]])    
    
    

# To debug: print("Debug messages...", file=sys.stderr)


