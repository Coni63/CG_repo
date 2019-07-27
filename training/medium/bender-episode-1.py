import sys
import math

toEnglish = {"SUD":"SOUTH", "EST":"EAST", "NORD":"NORTH", "OUEST":"WEST"}

class Bender:
    def __init__(self, x, y):
        self.sens = "NORMAL"
        self.orientation = "SUD"
        self.position_x = x
        self.position_y = y
        self.mode = "BASE"
        
    def change_direction(self, obstacle):
        if obstacle =="S":
             self.orientation = "SUD"
        elif obstacle =="E":
             self.orientation = "EST"
        elif obstacle =="N":
             self.orientation = "NORD"
        elif obstacle =="W":
             self.orientation = "OUEST"
    
    def inverser(self):
        if self.sens == "NORMAL":
            self.sens = "INVERT"
        else:
            self.sens = "NORMAL"
        #print("inversion...", file=sys.stderr)
            
    def boire(self):
        if self.mode == "CASSEUR":
            self.mode = "BASE"
        elif self.mode == "BASE":
            self.mode = "CASSEUR"
        #print("et glou et glou et glou...", file=sys.stderr)
            
    def teleport(self, a, b):
        self.position_x = a
        self.position_y = b
        #print("teleportation activé...", file=sys.stderr)
        
    def avancer(self):
        if self.orientation == "SUD":
            self.position_y += 1
        elif self.orientation == "EST":
            self.position_x += 1
        elif self.orientation == "NORD":
            self.position_y -= 1
        elif self.orientation == "OUEST":  
            self.position_x -= 1
        return [self.position_x, self.position_y]
            
    def reculer(self):
        if self.orientation == "SUD":
            self.position_y -= 1
        elif self.orientation == "EST":
            self.position_x -= 1
        elif self.orientation == "NORD":
            self.position_y += 1
        elif self.orientation == "OUEST":  
            self.position_x += 1
            
    def check_around(self, carte):
        flag_local = True
        south = carte[self.position_y+1][self.position_x]
        north =carte[self.position_y-1][self.position_x]
        west = carte[self.position_y][self.position_x-1]
        east = carte[self.position_y][self.position_x+1]
        print(south+north+west+east, file=sys.stderr)
        if self.sens == "NORMAL":    
            if south not in ["X", "#"] or (south == "X" and self.mode == "CASSEUR"):
                self.orientation = "SUD"
                character = south
            elif east not in ["X", "#"] or (east == "X" and self.mode == "CASSEUR"):
                self.orientation = "EST"
                print("go est", file=sys.stderr)
                character = east
            elif north not in ["X", "#"] or (north == "X" and self.mode == "CASSEUR"):
                self.orientation = "NORD"
                character = north
            elif west not in ["X", "#"] or (west== "X" and self.mode == "CASSEUR"):
                self.orientation = "OUEST"
                character = west
        else:
            if west not in ["X", "#"] or (west == "X" and self.mode == "CASSEUR"):
                self.orientation = "OUEST"
                character = west
            elif north not in ["X", "#"] or (north == "X" and self.mode == "CASSEUR"):
                self.orientation = "NORD"
                character = north
            elif east not in ["X", "#"] or (east == "X" and self.mode == "CASSEUR"):
                self.orientation = "EST"
                character = east
            elif south not in ["X", "#"] or (south == "X" and self.mode == "CASSEUR"):
                self.orientation = "SUD"
                character = south
        
        print(character, file=sys.stderr)
        posi = robot.avancer()
        path2.append(toEnglish[robot.orientation])
        
        if character in ["N","S","E","W"]:
            robot.change_direction(character)
        elif character == "B":
            robot.boire()
        elif character == "I":
            robot.inverser()
        elif character == "T":
            if posi == teleporteur[0]:
                robot.teleport(teleporteur[1][0], teleporteur[1][1])
            else:
                robot.teleport(teleporteur[0][0], teleporteur[0][1])
        elif character == "$":
            print(path2, file=sys.stderr)
            flag_local = False
            for each in path2:
                print(each)
        
        return flag_local
            
    def read_char(self, char):
        booleen = True
        if char == "#" or (char == "X" and robot.mode == "BASE"):
            robot.reculer()
            booleen = robot.check_around(la_map)
        elif char == "X" and robot.mode == "CASSEUR":
            la_map[robot.position_y][robot.position_x]=" "
            path2.append(toEnglish[robot.orientation])
        elif char in ["N","S","E","W"]:
            path2.append(toEnglish[robot.orientation])
            robot.change_direction(char)
        elif char == "B":
            robot.boire()
            path2.append(toEnglish[robot.orientation])
        elif char == "I":
            robot.inverser()
            path2.append(toEnglish[robot.orientation])
        elif char == "T":
            if posi == teleporteur[0]:
                robot.teleport(teleporteur[1][0], teleporteur[1][1])
            else:
                robot.teleport(teleporteur[0][0], teleporteur[0][1])
            path2.append(toEnglish[robot.orientation])
        else:
            path2.append(toEnglish[robot.orientation])
        
        return booleen
             
la_map = []
teleporteur = []

l, c = [int(i) for i in input().split()]
for i in range(l):
    row = input()
    if "T" in row:
        teleporteur.append([row.index("T"), i])
    if "@" in row:
        robot = Bender(row.index("@"), i)
    
    la_map.append(list(row))
    print(list(row), file=sys.stderr)

#print(str(robot.position_x)+","+str(robot.position_y), file=sys.stderr)
#print(teleporteur, file=sys.stderr)

posi = []
flag = True
turn = 0
max_turn = max(5*(l-2)*(c-2), 50)
path2 = []

while flag:
    turn += 1
    posi = robot.avancer()
    char1 = la_map[robot.position_y][robot.position_x]
    if char1 != "$" and turn < max_turn:
        flag = robot.read_char(char1)
    elif turn == max_turn:   
        flag = False
        print("LOOP")
    elif char1 == "$":
        path2.append(toEnglish[robot.orientation])
        flag = False
        for each in path2:
            print(each) 
   
# To debug: print("Debug messages...", file=sys.stderr)