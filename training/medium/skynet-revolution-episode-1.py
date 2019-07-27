import sys
import math
from operator import itemgetter

#####################

class Graphe(object):
	"""Classe représentant un graphe par un dictionnaire."""
	
	def __init__(self):
		"""Initialise le graphe à vide."""
		self.graphe = {}

	def ajouteSommet(self, sommet):
		"""Ajoute un sommet au graphe sans aucun voisin."""
		if sommet not in self.graphe.keys():
			self.graphe[sommet] = []

	def ajouteArrete(self, sommet, sommetVoisin):
		"""Crée une arrête en reliant sommet avec sommetVoisin en associant le poids p."""
		if sommet != sommetVoisin:
			self.graphe[sommetVoisin].append(sommet)
			self.graphe[sommet].append(sommetVoisin)

	def supprimeSommet(self, sommet):
		"""Supprime un sommet du graphe."""
		for sommetVoisin in self.graphe[sommet]:
			self.graphe[sommetVoisin].remove(sommet)
		del self.graphe[sommet]

	def supprimeArrete(self, sommet, sommetVoisin):
		"""Supprime une arrête."""
		#if sommet in self.graphe[sommetVoisin]:
		#	self.supprimeSommet(sommet)
		#	self.supprimeSommet(sommetVoisin)

		self.graphe[sommetVoisin].remove(sommet)
		self.graphe[sommet].remove(sommetVoisin)
		print(sommet, sommetVoisin)

	def toMatrice(self):
		"""Affichage matriciel du graphe."""
		txt = "  "
		for i in sorted(self.graphe.keys()):
		    txt += str(i)+"-"
		print(txt, file=sys.stderr)
		
		txt=""
		for i in sorted(self.graphe.keys()):
			txt += str(i)
			for j in sorted(self.graphe.keys()):
				if i in self.graphe[j].keys():
					txt += " 1"
				else:
					txt += " 0"
			print(txt, file=sys.stderr)
			txt = ""


node, link, gate = [int(i) for i in input().split()]
graph = Graphe()
list_node = []
list_gate = []
list_2 = []

for i in range(node):
    graph.ajouteSommet(i)
    list_node.append(i)

for i in range(link):
    n1, n2 = [int(j) for j in input().split()]
    graph.ajouteArrete(n1, n2)

for i in range(gate):
    ei = int(input())  # the index of a gateway node
    list_gate.append(ei)

print(graph.graphe, file=sys.stderr)
print(list_gate, file=sys.stderr)
print("****************", file=sys.stderr)

for each in list_node:
    if len(graph.graphe[each]) == 3:
        for each_other in graph.graphe[each]:
            if len(graph.graphe[each_other]) == 4:
                list_2.append([each, each_other]) 

sorted(list_2, key=itemgetter(1))
list_2.reverse()

while True:
    skynet = int(input())  # The index of the node on which the Skynet agent is positioned this turn
    
    print(graph.graphe, file=sys.stderr)
    print(list_gate, file=sys.stderr)
    print("****************", file=sys.stderr)
    print(list_2, file=sys.stderr)
    print("****************", file=sys.stderr)
    
    flag = False
    res = []
    
    if flag == False :
        for each in list_gate:
            if len(graph.graphe[each]) > 0:
                print(graph.graphe[each], file=sys.stderr)
                if skynet in graph.graphe[each]: # si skynet est voisin a un gate
                    graph.supprimeArrete(each, skynet)
                    flag = True
                     
    
    if flag == False :
        if len(list_2)>0:
            a = list_2.pop()
            graph.supprimeArrete(a[0], a[1])
            flag = True  
            
    if flag == False:
        for each in list_gate:
            if len(graph.graphe[each]) > 0:
                graph.supprimeArrete(each, graph.graphe[each][0])

#print(str(res[0])+" "+ str(res[1]))

#    if flag == False:
#        for each in list_gate:
#            inter_node = list(set(graph.graphe[skynet]) & set(graph.graphe[each])) #get list of node between a gate and skynet
#            if len(inter_node) > 2: #if there is more than 2 path to reach a gate
#                for middle_node in inter_node: # pour chaque node intermediaire
#                    hub_in_touch = list(set(graph.graphe[middle_node]) & set(list_gate)) #on recup les hub en contact
#                    if len(hub_in_touch) >= 2: #si le noeud est lié a 2+ gate
#                        graph.supprimeArrete(middle_node, list(hub_in_touch)[0])
#                        flag = True
#                
#    if flag == False:
#        if each in list_node:
#            if each not in list_gate:
#                hub_in_touch = list(set(graph.graphe[each]) & set(list_gate)) #on recup les hub en contact
#                if len(hub_in_touch) >= 2: #si le noeud est lié a 2+ gate
#                    graph.supprimeArrete(each, list(hub_in_touch)[0])
#                    flag = True
