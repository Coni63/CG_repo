import sys
import math
import time
from collections import defaultdict

class grid():
    def __init__(self, la_map):
        self.grille = la_map
    
    def show(self):
        for each_line in self.grille:
            print(each_line, file=sys.stderr)
            
    def update_map(self, pos1, pos2, dist):
        for y in range(h):
            for x in range(w):
                if self.grille[y][x] == 0:
                    if (x,y) in memo_dist.keys():
                        dist1 = memo_dist[(x,y)]
                    else:    
                        dist1 = (pos1[0]-x)**2+(pos1[1]-y)**2 #distance from previous point 
                    dist2 = (pos2[0]-x)**2+(pos2[1]-y)**2 #distance from latest position
                    memo_dist[(x,y)]=dist2
                    if dist == "COLDER" and dist1 > dist2: #si on s'eloigne et que la distance d'origine est plus grande que la nouvelle
                        self.grille[y][x]=1
                        del memo_dist[(x,y)]
                    elif dist == "WARMER" and dist2 > dist1:
                        self.grille[y][x]=1
                        del memo_dist[(x,y)]
                    elif dist == "SAME" and dist1 != dist2:
                        self.grille[y][x]=1
                        del memo_dist[(x,y)]
        self.grille[pos1[1]][pos1[0]]
                    
class aDallas():
    def __init__(self, X0, Y0):
        self.position = (X0, Y0)
        self.previous_position = (-1,-1)
        self.distance = "UNKNOWN"
        
    def move(self, new_x, new_y):
        global tower
        tower.grille[new_y][new_x] = 1
        self.previous_position = self.position
        self.position = (new_x, new_y)
        print(str(new_x), str(new_y))
    
    def update_sensor(self, result):
        self.distance = result

    def first_move(self):
        self.move((w-1)-self.position[0], (h-1)-self.position[1])
        
    
    def next_move(self, carte):
        max_dist = 0
        position = (0,0)
        for y in range(h):
            for x in range(w):
                if carte[y][x]==0:
                    dist = memo_dist[(x,y)]
                    if dist > max_dist:
                        max_dist = dist
                        position = (x,y)
        self.move(position[0], position[1])
                    
memo_dist = defaultdict(list)        
# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
carte = [[0 for x in range(w)] for x in range(h)] 
tower = grid(carte)
#tower.show()

n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]
batman = aDallas(x0, y0)
start_time_global = time.time() 
# game loop
while True:
    bomb_dir = input()  # Current distance to the bomb compared to previous distance (COLDER, WARMER, SAME or UNKNOWN)
    if bomb_dir == "UNKNOWN":
        batman.first_move()
    else:
        print(bomb_dir, file=sys.stderr)
        start_time_round = time.time()  
        batman.update_sensor(bomb_dir)
        tower.update_map(batman.previous_position, batman.position, batman.distance)
        #tower.show()
        batman.next_move(tower.grille)
        interval = time.time() - start_time_round     
        print("Round time : ", interval, file=sys.stderr)
        interval_global = time.time() - start_time_global     
        print("Total time : ", interval_global, file=sys.stderr)


    
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)


