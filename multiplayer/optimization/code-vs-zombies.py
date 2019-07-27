import sys
import math

class Human:
    def __init__(self, X, Y, ID):
        self.x = X
        self.y = Y
        self.id = ID
        self.distances = {}
        
        
    def update(self, X, Y):
        self.x = X
        self.y = Y
        
    def set_distances(self, instance, speed=400):
        for zombie in instance:
            d = math.sqrt((self.x - zombie.x)**2 + (self.y - zombie.y)**2)
            self.distances[zombie] = d//speed
            
    def goto(self, target):
        print("{} {}".format(target.x, target.y))
        
    def __repr__(self):
        return "H{}".format(self.id)

class Zombie:
    def __init__(self, ID, X, Y, next_X, next_Y):
        self.x = X
        self.y = Y
        self.id = ID
        self.nx = next_X
        self.ny = next_Y
        
    def update(self, X, Y, next_X, next_Y):
        self.x = X
        self.y = Y
        self.nx = next_X
        self.ny = next_Y

    def __repr__(self):
        return "Z{}".format(self.id)

me = Human(0, 0, 999)
while True:
    x, y = [int(i) for i in input().split()]
    me.update(x, y)
    
    Human_instances = []
    human_count = int(input())
    for i in range(human_count):
        human_id, human_x, human_y = [int(j) for j in input().split()]
        Human_instances.append(Human(human_x, human_y, human_id))     
    
    Zombie_instances = []
    zombie_count = int(input())
    for i in range(zombie_count):
        zombie_id, zombie_x, zombie_y, zombie_xnext, zombie_ynext = [int(j) for j in input().split()]
        Zombie_instances.append(Zombie(zombie_id, zombie_x, zombie_y, zombie_xnext, zombie_ynext))
    
    me.distances = {}
    me.set_distances(Human_instances, speed=1000)
    print(me.distances, file=sys.stderr)
    
    if human_count == 1:
        me.goto(Human_instances[0])
    else:
        closest = 30000
        need_protect = None
        for each_human in Human_instances:
            each_human.set_distances(Zombie_instances, speed = 400)
            print(each_human.distances, file=sys.stderr)   
            #if can be saved ...
            for key, dist in each_human.distances.items():
                if dist < closest and me.distances[each_human] < dist:
                    closest = dist
                    need_protect = each_human
            print(each_human.distances, file=sys.stderr)
        me.goto(need_protect) 
    