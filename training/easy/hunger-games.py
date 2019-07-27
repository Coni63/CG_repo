import sys
import math

class Player:
    def __init__(self, name):
        self.name = name
        self.killed = []
        self.killer = []
    
    def kill(self, other):
        self.killed.append(other.name)
        other.killer.append(self.name)
        
    def make_winner(self):
        self.killer = ["Winner"]
        
    def show(self, last):
        self.killed.sort()
        self.killer.sort()
        
        print("Name: {}".format(self.name))
        
        if len(self.killed) == 0:
            print("Killed: None")
        else:
            print("Killed: {}".format(", ".join(self.killed)))
        
        if len(self.killer) == 0:
            print("Killer: None")
        else:
            print("Killer: {}".format(", ".join(self.killer)))
        
        if not last:
            print("")


tributes = int(input())
p = [Player(input()) for i in range(tributes)]
p.sort(key = lambda x:x.name)
p_dict = {each.name : each for each in p}

turns = int(input())
for i in range(turns):
    a, b, *c = input().split()
    # print(a, b, c, file=sys.stderr)
    if isinstance(c, list):
        for each in c:
            p_dict[a].kill(p_dict[each.replace(",", "")])
    else:
        p_dict[a].kill(p_dict[c])

for each in p:
    if len(each.killer) == 0:
        each.make_winner()

for i, each in enumerate(p):
    last = (i+1) == tributes
    each.show(last)
