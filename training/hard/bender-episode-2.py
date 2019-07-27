import sys
import math

memo = {}

def max_money(ce_node):
    if ce_node in memo:
        return memo[ce_node]
    else:
        max_argent = 0
        for voisin in graph.graphe[ce_node]:
            a = max_money(voisin)+list_node[ce_node]
            max_argent = max(max_argent, a)
        memo[ce_node] = max_argent
        return max_argent

class Graphe(object):

	def __init__(self):
		self.graphe = {}

	def ajouteSommet(self, sommet):
		if sommet not in self.graphe.keys():# and sommet != "E":
			self.graphe[sommet] = []

	def ajouteArrete(self, sommet, sommetVoisin):
		if sommet != sommetVoisin:
			self.graphe[sommet].append(sommetVoisin)

	def supprimeSommet(self, sommet):
		for sommetVoisin in self.graphe[sommet].keys():
			del self.graphe[sommetVoisin][sommet]
		del self.graphe[sommet]

	def supprimeArrete(self, sommet, sommetVoisin):
		self.graphe[sommet].remove([sommetVoisin])

graph = Graphe()
list_node = {'E':0}

n = int(input())
for i in range(n):
    room = input()
    num, money, v1, v2 = room.split(" ")
    graph.ajouteSommet(num)
    graph.ajouteSommet(v1)
    graph.ajouteSommet(v2)
    graph.ajouteArrete(num, v1)
    graph.ajouteArrete(num, v2)
    list_node[num] = int(money)

#print(graph.graphe, file=sys.stderr)
#print(list_node, file=sys.stderr)

start = str(0)
total = list_node[start]

a = max_money(start)
print(a, file=sys.stderr)

#while graph.graphe[start] != ['E','E']:
#    max_money = 0
#    visited = 0
#    if graph.graphe[graph.graphe[start][0]] == ['E','E'] and graph.graphe[graph.graphe[start][1]] != ['E','E']:
#        max_money = list_node[graph.graphe[1]]
#        visited = graph.graphe[1]
#    elif graph.graphe[graph.graphe[start][1]] == ['E','E'] and graph.graphe[graph.graphe[start][0]] != ['E','E']:
#        max_money = list_node[graph.graphe[0]]
#        visited = graph.graphe[0]
#    elif graph.graphe[start][0] == 'E':
#        max_money = list_node[graph.graphe[start][1]]
#        visited = graph.graphe[start][1]
#    elif graph.graphe[start][1] == 'E':
#        max_money = list_node[graph.graphe[start][0]]
#        visited = graph.graphe[start][0]
#    else:
#        for each in graph.graphe[start]:
#            if list_node[each] > max_money:
#                max_money = list_node[each]
#                visited = each
#    
#    start = visited
#    total += max_money
    
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print(a)
