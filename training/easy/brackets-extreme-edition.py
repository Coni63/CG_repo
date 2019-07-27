import sys
import math
import re

crochet_ouvert = 0
accolade_ouvert = 0
parenthese_ouvert = 0
crochet_ferme = 0
accolade_ferme = 0
parenthese_ferme = 0

expression = input()

for char in expression:
    if char == "{":
        accolade_ouvert+=1
    elif char =="}"  and accolade_ouvert > 0:
        accolade_ferme+=1
    elif char =="(":
        parenthese_ouvert+=1
    elif char ==")"  and parenthese_ouvert > 0:
        parenthese_ferme+=1
    elif char =="[":
        crochet_ouvert+=1
    elif char =="]" and crochet_ouvert > 0:  
        crochet_ferme+=1
    elif char =="}" and accolade_ouvert == 0:
        accolade_ferme+=10000
    elif char ==")" and parenthese_ouvert == 0:
        parenthese_ferme+=10000
    elif char =="]" and crochet_ouvert == 0: 
        crochet_ferme+=10000

if crochet_ouvert == crochet_ferme and accolade_ouvert == accolade_ferme and parenthese_ouvert == parenthese_ferme:
    print("true")
else: 
    print("false")

# To debug: print("Debug messages...", file=sys.stderr)

