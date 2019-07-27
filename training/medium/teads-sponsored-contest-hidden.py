import sys
import math
from operator import itemgetter
import collections

def checkPath(child, parent=None):
    routeLength = 0
    for each_child in graph.graphe[child]: #for each node children of the parent
        if each_child == parent: #if it's the fater we continue to avoid infinite loop
            continue
        val = checkPath(each_child, child) #we run again the program to count child of child and so on
        if routeLength == 0 or routeLength < val: #will be used only on "main" loop
            routeLength = val
    if routeLength == 0: #used in child of child to count
        return 1
    else:
        return routeLength + 1

def merge_wo_duplicate(a,b):
    in_first = set(a)
    in_second = set(b)
    
    in_second_but_not_in_first = in_second - in_first
    
    result = a + list(in_second_but_not_in_first)
    return result

class Graphe(object):
	"""Classe représentant un graphe par un dictionnaire."""
	
	def __init__(self):
		"""Initialise le graphe à vide."""
		self.graphe = {}

	def ajouteSommet(self, sommet):
		"""Ajoute un sommet au graphe sans aucun voisin."""
		if sommet not in self.graphe.keys():
			self.graphe[sommet] = []
			list_node.append(sommet)

	def ajouteArrete(self, sommet, sommetVoisin):
		"""Crée une arrête en reliant sommet avec sommetVoisin en associant le poids p."""
		if sommet != sommetVoisin:
			self.graphe[sommetVoisin].append(sommet)
			self.graphe[sommet].append(sommetVoisin)


graph = Graphe()

n = int(input())  # the number of adjacency relations
list_node = []
list_x = []
list_y = []

for i in range(n):
    # xi: the ID of a person which is adjacent to yi
    # yi: the ID of a person which is adjacent to xi
    xi, yi = [int(j) for j in input().split()]
    list_x.append(xi)
    list_y.append(yi)
    graph.ajouteSommet(xi)
    graph.ajouteSommet(yi)
    graph.ajouteArrete(xi,yi)
    

start = set(list_x).difference(set(list_y)).pop() #the start is the node which is never a children
result = {}
vals = []

for each_child in graph.graphe[start]:
    vals.append(checkPath(each_child, start))

print(vals, file=sys.stderr)

vals.sort(key=lambda x: x)

if len(vals) > 1: #si le start se split direct
    vals.reverse()
    bestVal = vals[0] + vals[1]
else:
    bestVal = vals[0]

if bestVal % 2 != 0: #we check the middle of the line for example  3 <- 2 <- [1] -> 4 -> 5 or 1 -> 2 -> [3] -> 4 -> 5
    bestVal = bestVal / 2 + 1
else:
    bestVal /= 2

print(int(bestVal))

