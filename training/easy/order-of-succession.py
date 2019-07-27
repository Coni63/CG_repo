import sys
import math
import operator

class Person:
    def __init__(self, name, birth, death, religion, gender):
        self.name = name
        self.birth = int(birth)
        self.death = int(death) if death != "-" else None
        self.religion = religion
        self.gender = 1 if gender == "M" else 0
        
    def __repr__(self):
        return "{}-{}[{}]".format(self.gender, self.name, self.birth)


# Graph creation
graph = {}
root = None
for i in range(int(input())):
    name, parent, birth, death, religion, gender = input().split()
    p = Person(name, birth, death, religion, gender)
    if parent != "-": 
        graph[parent].append(p)
    if i == 0:
        root = p
    graph[name] = []

# Graph sort
for key, value in graph.items():
    value.sort(key = lambda x:(x.gender, -x.birth), reverse=True)

# DFS
queue = [root]
while len(queue) > 0:
    item = queue.pop(0)
    if item.death is None and item.religion != "Catholic":
        print(item.name)
    queue = graph[item.name] + queue

