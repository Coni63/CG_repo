import sys
import math

valeur = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7 , "8":8, "9":9, "10":10, "J":11, "Q":12, "K":13, "A":14}

class player:
    def __init__(self):
        self.carte = []
        self.tas = []
        print("joueur has " + str(len(self.carte)) + " card", file=sys.stderr)
    
    def gagne(self, c):
        self.carte.extend(c)
        
    def pose(self):
        return self.carte.pop(0) #retire de la liste et return la valeur
        
    def defausse(self):
        a = []
        for i in range(3):
            b = self.pose()
            a.append(b)
        return a

player1 = player()
player2 = player()

n = int(input())  # the number of cards for player 1
for i in range(n):
    cardp_1 = input()  # the n cards of player 1
    player1.gagne([cardp_1])
    
m = int(input())  # the number of cards for player 2
for i in range(m):
    cardp_2 = input()  # the m cards of player 2
    player2.gagne([cardp_2])

turn = 0  
tas1 = []
tas2 = []

while True:
    if len(player1.carte) == 0:
        print("2"+" "+str(turn))
        break
    elif len(player2.carte) == 0:
        print("1"+" "+str(turn))
        break
    else:
        c1 = player1.pose()
        c2 = player2.pose()
        tas1.append(c1)
        tas2.append(c2)
        print(c1+" vs "+c2, file=sys.stderr)
        if valeur[c1[:-1]] > valeur[c2[:-1]]:
            turn +=1
            player1.gagne(tas1 + tas2)
            tas1 = []
            tas2 = []
        elif valeur[c2[:-1]] > valeur[c1[:-1]]:
            turn +=1
            player2.gagne(tas1 + tas2)
            tas1 = []
            tas2 = []
            print(player2.carte, file=sys.stderr)
        else:
            if len(player1.carte) <= 3 or len(player2.carte) <= 3:
                print("PAT")
                break
            else :
                tas1 += player1.defausse()
                tas2 += player2.defausse()
                
# To debug: print("Debug messages...", file=sys.stderr)               
        