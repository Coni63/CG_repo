import sys
import math

class votant:    
    def __init__(self, name, nb):
        self.nom = name
        self.max_votes = int(nb)
        self.queue = []
        liste[self.nom] = self
        
    def voter(self, val):
        self.queue.append(val)
        
    def count(self):
        global vote
        if len(self.queue) <= self.max_votes:
            for val in self.queue:
                if val=="Yes":
                    vote["nb_yes"] += 1
                elif val=="No":
                    vote["nb_no"] += 1
                else:
                    vote["nb_blanc"] += 1
                print("%s a vote %s" % (self.nom, val), file=sys.stderr)

vote = {"nb_no" : 0, "nb_yes" : 0, "nb_blanc" : 0}
liste = {}

n = int(input())
m = int(input())

for i in range(n):
    person_name, nb_vote = input().split()
    votant(person_name, nb_vote) 

print(list(liste.keys()), file=sys.stderr)
    
for i in range(m):
    voter_name, vote_value = input().split()
    if voter_name in liste.keys():
        liste[voter_name].voter(vote_value)
    else:
        print("%s is not allowed to vote" %voter_name , file=sys.stderr)
        
for each in liste.keys():
    liste[each].count()
        
print(vote["nb_yes"], vote["nb_no"])
# To debug: print("Debug messages...", file=sys.stderr)