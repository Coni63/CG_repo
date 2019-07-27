import sys
import math
from collections import defaultdict, deque
from time import time

def dijkstra(graph, initial):
    visited = {initial: 0}
    path = {}

    nodes = set(graph.nodes)

    while nodes:
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node
        if min_node is None:
            break

        nodes.remove(min_node)
        current_weight = visited[min_node]

        for edge in graph.edges[min_node]:
            try:
                weight = current_weight + graph.distances[(min_node, edge)]
            except:
                continue
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge] = min_node

    return visited, path

def shortest_path(graph, origin, destination):
    visited, paths = dijkstra(graph, origin)
    full_path = deque()
    _destination = paths[destination]
    #dist = 0

    while _destination != origin:
        full_path.appendleft(_destination)
        _destination = paths[_destination]
        #dist += graph.distances[(paths[_destination],destination)]

    full_path.appendleft(origin)
    full_path.append(destination)

    return visited[destination], list(full_path)

class Graphe(object):
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def ajouteSommet(self, sommet):
        if sommet not in self.nodes:
            self.nodes.add(sommet)
            list_node.append(sommet)

    def ajouteArrete(self, sommet, sommetVoisin, dist=1):
        if sommet != sommetVoisin:
            self.edges[sommetVoisin].append(sommet) 
            self.edges[sommet].append(sommetVoisin)
            self.distances[(sommet, sommetVoisin)] = dist
            self.distances[(sommetVoisin, sommet)] = dist
            
    def retireArrete(self, sommet, sommetVoisin):
        if sommet != sommetVoisin:
            self.edges[sommetVoisin].remove(sommet)
            self.edges[sommet].remove(sommetVoisin)
            del self.distances[(sommet, sommetVoisin)]
            del self.distances[(sommetVoisin, sommet)]
            if len(self.edges[sommet]) == 0: self.nodes.remove(sommet)
            if len(self.edges[sommetVoisin]) == 0: self.nodes.remove(sommetVoisin)
            print(sommet, sommetVoisin)


def update_distance():
    for each in list_node:
        hub_in_touch = list(set(graph.edges[each]) & set(list_gate)) #on recup les hub en contact
        
        if len(hub_in_touch) == 2 and each not in critical_node: #si le noeud est lié a 2 gate
            critical_node.append(each)
        
        if len(hub_in_touch) == 1: #si le noeud est lié a un seul gate, on simplifie le graphe simplifie
            for other_node in graph.edges:
                test = list(set(graph.edges[other_node]) & set(list_gate))
                if len(test) > 0:
                    graph.distances[(each,other_node)] = 0
                    graph.distances[(other_node,each)] = 0

def direct_contact(list_A, item_B):
    for item in list_A: #Pour chaque gate
        if item_B in graph.edges[item]: #si skynet est dans un noeud adjacent
            graph.retireArrete(item, item_B) #on ferne ce noeud
            return True
    return False
    
def close_closest_critical_node(skynet):
    NodeA = None
    NodeB = None
    best_dist = float('inf')
    for double_path in critical_node:
        dist, path = shortest_path(graph, skynet, double_path)
        #print("Distance from %s to %s = %s (path = %s)" % (skynet, double_path, dist, path),file=sys.stderr)
        if dist <= best_dist:
            best_dist = dist
            NodeA = double_path
            for each_voisin in graph.edges[NodeA]:
                if each_voisin in list_gate:
                    NodeB = each_voisin
                    break
            
    graph.retireArrete(NodeA, NodeB)
    critical_node.remove(NodeA)
    update_distance()

def close_random_node():
    for each_gate in list_gate:
        if len(graph.edges[each_gate]) > 0:
            graph.retireArrete(each_gate, graph.edges[each_gate][0])
            update_distance()
            break

graph = Graphe()
list_gate = []
list_node = []
critical_node = []
dist = {}
order_gate = []

node, link, gate = [int(i) for i in input().split()]

for i in range(node):
    graph.ajouteSommet(i)

for i in range(link):
    n1, n2 = [int(j) for j in input().split()]

    graph.ajouteArrete(n1, n2)

print(graph, file=sys.stderr)

for i in range(gate):
    ei = int(input())  # the index of a gateway node
    list_gate.append(ei)


update_distance()

#print(shortest_path(graph, 0, 47), file = sys.stderr)
#print(graph.graphe, file=sys.stderr)
#print(list_gate, file=sys.stderr)
#print(critical_node, file=sys.stderr)
#print("****************", file=sys.stderr)
#print([(x, graph.edges[x]) for x in graph.nodes], file=sys.stderr)

while True:
    start = time()
    
    skynet = int(input())  # The index of the node on which the Skynet agent is positioned this turn
    
    if direct_contact(list_gate, skynet) == False:
        if len(critical_node) > 0:
            close_closest_critical_node(skynet)
        else:
            close_random_node()
    
    print((time()-start)*1000, file=sys.stderr)
            
   
    
    