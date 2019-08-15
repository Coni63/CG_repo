import sys
import math
import itertools

class Player:
    def __init__(self, num, pos):
        self.id = num
        self.pos = pos
        self.double_turn = 0
        self.jail = False
        self.jail_turn = 0
        
    def move(self, n):
        self.pos += n
        self.pos = self.pos%40
        if self.pos == 30:
            print("go to jail", self, file=sys.stderr)
            self.jail = True
            self.pos = 10
            return False
    
    def play(self, d1, d2):
        if self.jail:
            if d1 == d2:
                print("out of jail by double", self, file=sys.stderr)
                self.jail = False
                self.jail_turn = 0
                self.double_turn = 0
                self.move(d1+d2)
                return False
            else:
                self.jail_turn += 1
                if self.jail_turn == 3:
                    print("out of jail by timeout", self, file=sys.stderr)
                    self.jail = False
                    self.jail_turn = 0
                    self.move(d1+d2)
                    return False
        else:
            if d1 == d2:
                self.double_turn += 1
                if self.double_turn == 3:
                    print("too many double", self, file=sys.stderr)
                    self.jail = True
                    self.pos = 10
                    return False
                else:
                    self.move(d1+d2)
                    return not self.jail  # do not play again if your double sent you in prison
            else:
                self.double_turn = 0
                self.move(d1+d2)
                return False

                
        
    
    def __repr__(self):
        return f"{self.id} - {self.pos} - {self.jail}"
    
players = []  

p = int(input())
for i in range(p):
    name, pos = input().split()
    pos = int(pos)
    players.append(Player(name, pos))

players_iter = itertools.cycle(players)
curr_player = next(players_iter)

d = int(input())
for i in range(d):
    dice1, dice2 = [int(x) for x in input().split()]
    if curr_player.id == "Thimble":
        print(curr_player, "plays", dice1, dice2, file=sys.stderr)
    replay = curr_player.play(dice1, dice2)
    if not replay:
        curr_player = next(players_iter)
    
for i in range(40):
    boardline = input()

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

for player in players:
    print(player.id, player.pos)
