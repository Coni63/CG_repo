import sys
import math
from operator import itemgetter

def merge_wo_duplicate(a,b):
    in_first = set(a)
    in_second = set(b)
    
    in_second_but_not_in_first = in_second - in_first
    
    result = a + list(in_second_but_not_in_first)
    return result

def bfs(start, nb) :
    impacted=[start]
    impacted_prev_turn = [start]
    step = 0
    while len(impacted_prev_turn) > 0:
        impacted_this_turn = []
        for each_origin in impacted_prev_turn:
            impacted_this_turn = merge_wo_duplicate(impacted_this_turn, graph.graphe[each_origin])
                #impacted_this_turn += [i for i in graph.graphe[each] if i not in impacted_this_turn]
        impacted_prev_turn = impacted_this_turn
        impacted = merge_wo_duplicate(impacted, impacted_prev_turn)
        step += 1
    return step

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
			self.graphe[sommet].append(sommetVoisin)


graph = Graphe()
list_node = []

n = int(input())  # the number of relationships of influence
for i in range(n):
    # x: a relationship of influence between two people (x influences y)
    x, y = [int(j) for j in input().split()]
    graph.ajouteSommet(x)
    graph.ajouteSommet(y)
    graph.ajouteArrete(x,y)

print(graph.graphe, file=sys.stderr)

longest_line = 0

for each_start in list_node:
    a = bfs(each_start, n)
    print(a, file=sys.stderr)
    if a > longest_line:
        longest_line = a

print(longest_line)

# To debug: print("Debug messages...", file=sys.stderr)

