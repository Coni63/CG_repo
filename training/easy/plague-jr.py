import sys
import math
import copy

class Node:
    def __init__(self, n):
        self.n = n
        self.link = set()
        self.alive = True
        
    def __len__(self):
        return len(self.link)
    
    def __repr__(self):
        return f"Node {self.n} - {self.link}"
        
    def add_node(self, other):
        self.link.add(other.n)
        other.link.add(self.n)
        
    def remove_node(self):
        other = self.link.pop()
        # print("Removing node between {} and {} ({} and {})".format(self.n, other, len(self), len(nodes[other])), file=sys.stderr)
        nodes[other].link.remove(self.n)
        self.update()
        nodes[other].update()
        
    def update(self):
        if len(self) == 0:
            self.alive = False

        
nodes = {}

n = int(input())
for i in range(n):
    a, b = [int(j) for j in input().split()]
    if a not in nodes:
        nodes[a] = Node(a)
    if b not in nodes:
        nodes[b] = Node(b)
    nodes[a].add_node(nodes[b])

# for key, node in nodes.items():
#     print(node, file=sys.stderr)

depth = 0
while sum([value.alive for key, value in nodes.items()]) >= 2:
    # print("Depth : {} - nodes : {}".format(depth, sum([value.alive for key, value in nodes.items()])), file=sys.stderr)
    to_process = []
    for key, value in nodes.items():
        if value.alive and len(value) == 1:
            to_process.append(key)

    for key in to_process:
        try:
            nodes[key].remove_node()
        except:
            pass # issue when 2 nodes remain with one link because they kill each other
            
    depth +=1
    
print(depth)

