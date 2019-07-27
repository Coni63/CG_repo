import sys
import math
import time
#from collections import defaultdict, deque
import heapq 

def dijkstra(adj, costs, s, t):
    ''' Return predecessors and min distance if there exists a shortest path 
        from s to t; Otherwise, return None '''
    Q = []     # priority queue of items; note item is mutable.
    d = {s: 0} # vertex -> minimal distance
    Qd = {}    # vertex -> [d[v], parent_v, v]
    p = {}     # predecessor
    visited_set = set([s])

    for v in adj.get(s, []):
        d[v] = costs[s, v]
        item = [d[v], s, v]
        heapq.heappush(Q, item)
        Qd[v] = item

    while Q:
        #print(Q)
        cost, parent, u = heapq.heappop(Q)
        if u not in visited_set:
            #print 'visit:', u
            p[u]= parent
            visited_set.add(u)
            if u == t:
                return p, d[u]
            for v in adj.get(u, []):
                if d.get(v):
                    if d[v] > costs[u, v] + d[u]:
                        d[v] =  costs[u, v] + d[u]
                        Qd[v][0] = d[v]    # decrease key
                        Qd[v][1] = u       # update predecessor
                        heapq._siftdown(Q, 0, Q.index(Qd[v]))
                else:
                    d[v] = costs[u, v] + d[u]
                    item = [d[v], u, v]
                    heapq.heappush(Q, item)
                    Qd[v] = item

    return None

def make_undirected(cost):
    ucost = {}
    for k, w in cost.items():
        ucost[k] = w
        ucost[(k[1],k[0])] = w
    return ucost

class arret():
    def __init__(self, stop):
        stop = stop.split(",")
        self.ID = stop[0][len(prefix_Station):]
        self.name = stop[1][1:-1]
        self.description = stop[2]
        self.latitude = math.radians(float(stop[3]))
        self.longitude = math.radians(float(stop[4]))
        self.zone = stop[5]
        self.url = stop[6]
        self.type_arret = stop[7]
        self.station_parent = stop[8]
        list_arret[self.ID]=self #on retourne dans un dictionnaire l'objet lie a son ID
    
    def get_dist(self, node2):
        x = (node2.longitude-self.longitude)*math.cos((self.longitude+node2.longitude)/2)
        y = node2.latitude-self.latitude
        d = 6371*math.sqrt(x**2+y**2)
        return d
        

class Graphe(object):
	def __init__(self):
		self.graphe = {}

	def ajouteSommet(self, sommet):
		if sommet not in self.graphe.keys():
			self.graphe[sommet] = []

	def ajouteArrete(self, sommet, sommetVoisin):
		self.graphe[sommet].append(sommetVoisin)
		
start_time = time.time()  
graph = Graphe()
list_arret = {}
prefix_Station = 'StopArea:'
cost = {}

start_point = input()[len(prefix_Station):]
end_point = input()[len(prefix_Station):]

n = int(input())
for i in range(n):
    stop_name = input()
    arret(stop_name)  

m = int(input())
for i in range(m):
    route = input()
    route = route.split()
    depart = route[0][len(prefix_Station):]
    arrive = route[1][len(prefix_Station):]
    if depart != arrive:
        graph.ajouteSommet(depart)
        graph.ajouteSommet(arrive)
        distance = list_arret[depart].get_dist(list_arret[arrive])
        cost[(depart, arrive)]=distance
        graph.ajouteArrete(depart, arrive)
        
cost = make_undirected(cost)

try:
    if start_point == end_point:
        print(list_arret[start_point].name)
    else:
        #result = shortest_path(graph.graphe, start_point, end_point)
        #print('Distance mini = ', result, file=sys.stderr)
        predecessors, min_cost = dijkstra(graph.graphe, cost, start_point, end_point)
        trajet = []
        extremite = end_point
        while extremite != start_point:   
            trajet = [extremite] + trajet
            extremite = predecessors[extremite]
        trajet = [start_point] + trajet
        for each in trajet:
            print(list_arret[each].name)
except:
    print("IMPOSSIBLE")

interval = time.time() - start_time     
print("Total time in seconds : ", interval, file=sys.stderr)

# To debug: print("Debug messages...", file=sys.stderr)