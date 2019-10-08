import sys
import math
import time
from collections import defaultdict

class Link:
    def __init__(self, ID, node1, node2):
        self.ID = ID
        self.node1 = node1
        self.node2 = node2
        self.validated = False
        self.strength = 0
        
    def __repr__(self):
        res = f"Link {self.ID} - ({self.node1.col}, {self.node1.row}) => ({self.node2.col}, {self.node2.row}) [{self.strength}]"
        res += " validated" * self.validated
        res += " impossible" * (self.strength == -1)
        return res

    def __hash__(self):
        a, b = max(self.node1.ID, self.node2.ID), min(self.node1.ID, self.node2.ID)
        return 1000 * b + a

    def cross(self, other):
        if self.isVertical() and other.isHorizontal():
            ymin, ymax = self.getVrange()
            xmin, xmax = other.getHrange()
            return (ymin < other.node1.row < ymax) and (xmin <= self.node1.col <= xmax)
        elif self.isHorizontal() and other.isVertical():
            xmin, xmax = self.getHrange()
            ymin, ymax = other.getVrange()
            return (xmin < other.node1.col < xmax) and (ymin <= self.node1.row <= ymax)
        else:
            return False
    
    def validate(self, strength, validated = False):
        # print(f"Validating link ({self.node1.col}, {self.node1.row}) - ({self.node2.col}, {self.node2.row}) with strength {strength}", file=sys.stderr)
        self.validated = validated            
        self.strength += strength
        for crossing_link in compatibility.get(self, []):
            if not crossing_link.impossible:
                crossing_link.block()
        
    def unvalidate(self, strength):
        self.validated = False
        self.strength -= strength
        for crossing_link in compatibility.get(self, []):
            if crossing_link.impossible:
                crossing_link.unblock()
    
    def show(self):
        print(f"{self.node1.col} {self.node1.row} {self.node2.col} {self.node2.row} {self.strength}")
    
    def block(self):
        self.strength = -1
        
    def unblock(self):
        self.strength = 0
    
    def isVertical(self):
        return self.node1.col == self.node2.col

    def isHorizontal(self):
        return self.node1.row == self.node2.row
        
    def getHrange(self):
        return min(self.node1.col, self.node2.col), max(self.node1.col, self.node2.col)
    
    def getVrange(self):
        return min(self.node1.row, self.node2.row), max(self.node1.row, self.node2.row)
        
    @property
    def impossible(self):
        return self.strength == -1

class Node:
    def __init__(self, col, row, strength):
        self.ID = len(nodes)
        self.col = col
        self.row = row
        self.default_strength = strength
        self.links = []
        nodesByPosition[(self.row, self.col)] = self
    
    def __repr__(self):
        result = f"Node {self.ID} - ({self.col}, {self.row}) - Weight {self.strength} - "
        result += ",".join(str(x.ID) for x in self.links)
        return result
        
    def __len__(self):
        return len(self.links)
    
    @property
    def strength(self):
        return self.default_strength - sum(link.strength for link in self.links if link.strength > 0)
    
    def remaining_links(self):
        return [x for x in self.links if x.strength != -1 and not x.validated] 
        
    @property
    def strength2(self):
        return self.default_strength
        
    def remaining_links2(self):
        return [x for x in self.links if x.strength != -1] 
                
    def add(self, link):
        if link not in self.links:
            self.links.append(link)

def build_graph():
    def is_possible(link):
        if link.node1.default_strength == 1 and link.node2.default_strength == 1 and len(nodes) > 2:
            return False
        else:
            return True
    
    links = []
    hashes_links = set()
    for i, node in enumerate(nodes):
        row, col = node.row, node.col
        
        # look up
        for i in range(row-1, -1, -1):
            other = nodesByPosition.get((i, col), None)
            if other is not None:
                l = Link(len(links), node, other)
                if hash(l) not in hashes_links and is_possible(l):
                    hashes_links.add(hash(l))
                    links.append(l)
                    node.add(l)
                    other.add(l)
                break
                
        # look down
        for i in range(row+1, height):
            other = nodesByPosition.get((i, col), None)
            if other is not None:
                l = Link(len(links), node, other)
                if hash(l) not in hashes_links and is_possible(l):
                    hashes_links.add(hash(l))
                    links.append(l)
                    node.add(l)
                    other.add(l)
                break
                
        # look left
        for i in range(col-1, -1, -1):
            other = nodesByPosition.get((row, i), None)
            if other is not None:
                l = Link(len(links), node, other)
                if hash(l) not in hashes_links and is_possible(l):
                    hashes_links.add(hash(l))
                    links.append(l)
                    node.add(l)
                    other.add(l)
                break
                
        # look right
        for i in range(col+1, height):
            other = nodesByPosition.get((row, i), None)
            if other is not None:
                l = Link(len(links), node, other)
                if hash(l) not in hashes_links and is_possible(l):
                    hashes_links.add(hash(l))
                    links.append(l)
                    node.add(l)
                    other.add(l)
                break
    return links

def makeSafePrediction():
    def ValidatesNodesWith1Neighbor():
        """
        Every nodes with only 1 neighbor can be directly validated. There is no other options. This reduce on some cases the problem
        """
        changes = 0
        for node in nodes:
            if node.strength == 0:
                continue
            r = node.remaining_links()
            if len(r) == 1:
                r[0].validate(node.strength, validated=True)
                changes += 1
        return changes
                
    def ValidateNodes468():
        """
        Every nodes with only a weigth = 2x number of neigthbor can be directly validated
        """
        changes = 0
        for node in nodes:
            if node.strength == 0:
                continue
            r = node.remaining_links2()
            if 2*len(r) == node.strength2:
                for link in r:
                    if not link.validated:
                        link.validate(2, validated=True)
                        changes += 1
        return changes
                        
    def ValidatePartialLinks():
        """
        Every nodes with only a weigth = 2x number of neigthbor can be directly validated
        """
        changes = 0
        for node in nodes:
            if node.strength == 0:
                continue
            r = node.remaining_links2()
            if 2*len(r)-1 == node.strength2:
                for link in r:
                    if link.strength == 0:
                        link.validate(1, validated=False)
                        changes += 1
        return changes
    
    def DeleteNonPossibleLinks():
        """
        Every node crossing a validated node can be removed from the search space
        """
        changes = 0
        # remove remaining links to nodes with no strength anymore
        for node in nodes:
            if node.strength == 0:
                for link in node.links:
                    if link.strength > 0:
                        link.validated = True
                    elif link.impossible == False:
                        link.block()
                        changes += 1
        return changes
                

    while True:
        global_change = 0
        
        while True:
            changes = ValidatesNodesWith1Neighbor()
            if changes == 0:
                break
            else:
                global_change += 1
        
        while True:
            changes = ValidateNodes468()
            if changes == 0:
                break
            else:
                global_change += 1
                
        while True:
            changes = ValidatePartialLinks()
            if changes == 0:
                break
            else:
                global_change += 1
                
        while True:
            changes = DeleteNonPossibleLinks()
            if changes == 0:
                break
            else:
                global_change += 1
                
        if global_change == 0:
            break
        
        
    
def isValid(link, strength):
    """
    return True if the link doesn't cross another one and if the strength is not too big
    """
    if len(nodes) > 2 and link.node1.strength == 2 and link.node2.strength == 2 and strength == 2:
        return False
    
    if strength > min(link.node1.strength, link.node2.strength):
        return False
        
    if link.strength + strength > 2:
        return False
    
    return True
        
def isSolved():
    """
    The game is considered solve if all the nodes have no other connections possible and all in one connected graph
    """
    def isOneGraph():
        q = [nodes[0]]
        visited = set()
        while len(q) > 0:
            node = q.pop(0)
            visited.add(node)
            for link in node.links:
                if link.strength > 0:
                    if link.node1 not in visited:
                        q.append(link.node1)
                    elif link.node2 not in visited:
                        q.append(link.node2)
        return len(visited) == len(nodes)
    
    remaining_weight = sum([node.strength for node in nodes])
    if remaining_weight == 0:
        return isOneGraph()
    else:
        return False

def solve(node):
    
    if isSolved():
        return True
    else:
        for i, link in enumerate(node.links):
            if link.validated or link.impossible:
                continue
            for k in [2, 1]:
                if isValid(link, k):
                    link.validate(k)
                    next_node = min(nodes, key = lambda x:x.strength if x.strength > 0 else 1e6)
                    if solve(next_node):
                        return True
                    link.unvalidate(k)

def buildCompatibilityGraph(links):
    """
    Return a graph which provides all links impossible if a given node is validated
    """
    G = defaultdict(list)
    for i, linka in enumerate(links):
        for j, linkb in enumerate(links[i+1:]):
            if linka.cross(linkb):
                G[linka].append(linkb)
                G[linkb].append(linka)
    return G

nodesByPosition = {}     
nodes = []
width = int(input())   # the number of cells on the X axis
height = int(input())  # the number of cells on the Y axis
for row in range(height):
    line = input()      # width characters, each either a number or a '.'
    for col in range(width):
        if line[col] != '.':
            nodes.append(Node(col, row, int(line[col])))

"""
To debug a validator not working
"""
# grid = [
#     "3.....1..", 
#     ".2..4..21", 
#     ".3.2..1..", 
#     "..2.5.3..", 
#     ".3...3.3.", 
#     "......2..", 
#     "..2..3..3", 
#     ".3..3.3..",
#     "3......44"]
    
# nodesByPosition = {}     
# nodes = []  
# width = 9   # the number of cells on the X axis
# height = 9 # the number of cells on the Y axis
# for row in range(height):
#     line = grid[row]      # width characters, each either a number or a '.'
#     for col in range(width):
#         if line[col] != '.':
#             n = int(line[col])
#             nodes.append(Node(col, row, int(line[col])))

start = time.time()    

links = build_graph()
compatibility = buildCompatibilityGraph(links)
makeSafePrediction()

# print(f"Number of Nodes : {len(links)}", end="\n\n", file=sys.stderr)
# print(*nodes, sep="\n", end="\n\n", file=sys.stderr)
# print(*links, sep="\n", end="\n\n", file=sys.stderr)

starting_node = min(nodes, key = lambda x:x.strength if x.strength > 0 else 1e6)
solve(starting_node)

# print(*nodes, sep="\n", end="\n\n", file=sys.stderr)
# print(*links, sep="\n", end="\n\n", file=sys.stderr)

for link in links:
    if link.strength > 0:
        link.show()
        
print(time.time()-start, file=sys.stderr)

