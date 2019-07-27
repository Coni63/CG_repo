import sys
import math
from time import time

"""https://pdfs.semanticscholar.org/1ae1/9e3cbdb46ea671d6b204355ebc37e9732e77.pdf"""

def apply_rule_1():
    """
    This function remove all possible links if
        - both nodes are with a weigth of 1
        - both nodes are with a weight of 2 and the link is double
        - one of the node is one and the link is double => moved to apply_rule_1_2
    """
    to_delete = []
    for key, link in Links.instances.items():
        if link.node1.link_possible == 1 and link.node2.link_possible == 1:
            to_delete.append(key)
        elif link.node1.link_possible == 2 and link.node2.link_possible == 2 and link.strength == 2:
            to_delete.append(key)
    
    #print(to_delete, file=sys.stderr)
    for each in to_delete:
        del Links.instances[each]
            

def apply_rule_1_2():
    to_delete = []
    for key, link in Links.instances.items():
        if (link.node1.link_possible == 1 or link.node2.link_possible == 1) and link.strength == 2:
                to_delete.append(key)
    for each in to_delete:
        del Links.instances[each]


def apply_rule_2():
    """
    This function check all links of a Node. If we can create only 1 link, we return it to be created else we return None and go for the next check
    """
    #print( ">>> New Check <<<<" ,file = sys.stderr)
    for key, node in Node.instances.items():
        possible_links = list(filter(lambda x: x.node1 == node or x.node2 == node, Links.instances.values()))
        #print( "Node {},{} - {}".format(node.x, node.y, possible_links) ,file = sys.stderr)
        if len(possible_links) == 1:
            return possible_links[0]
    return None


def apply_rule_3():
    """
    This function check all nodes which have only 1 other node
    """
    for node in Node.instances.values():
        other_links = list(filter(lambda x: x.node1 == node or x.node2 == node, Links.instances.values()))
        other_node = []
        link_involved = []
        for link in other_links:
            if link.node1 != node and link.node1 not in other_node and link.strength == node.link_possible:
                other_node.append(link.node1)
                link_involved.append(link)
            if link.node2 != node and link.node2 not in other_node and link.strength == node.link_possible:
                other_node.append(link.node2)
                link_involved.append(link)
                
        print(other_node, file=sys.stderr)
        
        if len(other_node) == 1:
            return (link_involved[0])
    return None


class Links():
    instances = {}
    def __init__(self, node1, node2, qte = 1):
        self.ID = len(self.instances.keys())+1
        self.node1 = node1
        self.node2 = node2
        self.strength = qte
        self.instances[self.ID] = self
        
    def create(self):
        print(self.node1.x, self.node1.y, self.node2.x, self.node2.y, self.strength)
        
        """ Suppression des autres liens entre les meme noeuds """
        node_involved = set([self.node1, self.node2])
        to_delete = list(filter(lambda x: set([x.node1, x.node2]) == node_involved, Links.instances.values()))
        #print("DELETE : " , to_delete, file=sys.stderr)
        for each in to_delete:
            del Links.instances[each.ID]
            
        """ Update de la strength des noeuds """
        self.node1.link_possible -= self.strength
        self.node2.link_possible -= self.strength
        
        """ Suppression des liens de chaque noeuds """
        self.node1.link_list.remove(self)
        self.node2.link_list.remove(self)
        
        
        """ Suppression des noeuds/liens a 0 """
        if self.node1.link_possible == 0:
            to_delete = list(filter(lambda x: x.node1 == self.node1 or x.node2 == self.node1, Links.instances.values()))
            #print("DELETE : " , to_delete, file=sys.stderr)
            for each in to_delete:
                del Links.instances[each.ID]
            del Node.instances[(self.node1.x, self.node1.y)]
        
        if self.node2.link_possible == 0:
            to_delete = list(filter(lambda x: x.node2 == self.node2 or x.node2 == self.node2, Links.instances.values()))
            #print("DELETE : " , to_delete, file=sys.stderr)
            for each in to_delete:
                del Links.instances[each.ID]
            del Node.instances[(self.node2.x, self.node2.y)]
            
        apply_rule_1_2()


class Node:
    instances = {}
    def __init__(self, X, Y, L):
        self.ID = len(self.instances.keys())+1
        self.x = X
        self.y = Y
        self.link_possible = L
        self.instances[(self.x, self.y)] = self
        self.up = None
        self.down = None
        self.left = None
        self.right = None
        self.link_list = []
        self.side = 0
        
    def __repr__(self):
        result = "Node {} - ({}, {}) - Weight {}".format(self.ID, self.x, self.y, self.link_possible)
        if self.up is not None: 
            result += " - Up : {}".format(self.up.ID)
        if self.down is not None: 
            result += " - Down : {}".format(self.down.ID)
        if self.left is not None: 
            result += " - Left : {}".format(self.left.ID)
        if self.right is not None: 
            result += " - Right : {}".format(self.right.ID)
        return result

    def set_links(self):
        if self.up is None:
            # print("checking up", file =sys.stderr)
            for i in range(self.y - 1, -1, -1):
                elem = Node.instances.get((self.x, i), None)
                if elem is not None:
                    # print("found node", elem.x, elem.y, file =sys.stderr)
                    self.up = elem
                    elem.down = self
                    self.create_link(elem)
                    break

        if self.down is None:
            # print("checking down", file =sys.stderr)
            for i in range(self.y + 1, height + 1):
                elem = Node.instances.get((self.x, i), None)
                if elem is not None:
                    # print("found node", elem.x, elem.y, file =sys.stderr)
                    self.down = elem
                    elem.up = self
                    self.create_link(elem)
                    break

        if self.left is None:
            # print("checking left", file =sys.stderr)
            for i in range(self.x - 1, -1, -1):
                elem = Node.instances.get((i, self.y), None)
                if elem is not None:
                    # print("found node", elem.x, elem.y, file =sys.stderr)
                    self.left = elem
                    elem.right = self
                    self.create_link(elem)
                    break

        if self.right is None:
            # print("checking right", file =sys.stderr)
            for i in range(self.x + 1, width + 1):
                elem = Node.instances.get((i, self.y), None)
                if elem is not None:
                    # print("found node", elem.x, elem.y, file =sys.stderr)
                    self.right = elem
                    elem.left = self
                    self.create_link(elem)
                    break
                    # print(node, file=sys.stderr)

    def create_link(self, other_node):
        L = Links(self, other_node)
        L2 = Links(self, other_node, 2)
        self.side += 1
        other_node.side += 1
        LG = [L, L2]
        self.link_list += LG
        other_node.link_list += LG
        return LG


width = int(input())  # the number of cells on the X axis
height = int(input())  # the number of cells on the Y axis
for y in range(height):
    line = input()  # width characters, each either a number or a '.'
    for x in range(width):
        if line[x] != '.':
            Node(x, y, int(line[x]))

start = time()    

for node in Node.instances.values():
    node.set_links()

print("Start : Nodes : {}, links : {}".format(len(Node.instances.keys()), len(Links.instances.keys())), file=sys.stderr)

apply_rule_1()

print("After Rule 1 : Nodes : {}, links : {}".format(len(Node.instances.keys()), len(Links.instances.keys())), file=sys.stderr)

apply_rule_1_2()

print("After Rule 1_2 : Nodes : {}, links : {}".format(len(Node.instances.keys()), len(Links.instances.keys())), file=sys.stderr)

link = -1
while link is not None:
    link = apply_rule_2()
    if link is not None:
        link.create()
        

print("After Rule 2 : Nodes : {}, links : {}".format(len(Node.instances.keys()), len(Links.instances.keys())), file=sys.stderr)

link = -1
while link is not None:
    link = apply_rule_3()
    if link is not None:
        link.create()
    
print("After Rule 2 : Nodes : {}, links : {}".format(len(Node.instances.keys()), len(Links.instances.keys())), file=sys.stderr)

print(time()-start, file=sys.stderr)
