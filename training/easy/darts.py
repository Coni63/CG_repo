import sys
import math

class Player:
    def __init__(self, name, num):
        self.name = name
        self.num = num
        self.score = 0
        
    def __repr__(self):
        return "{} {}".format(self.name, self.score)
        
players = {}
size = int(input())/2
n = int(input())
for i in range(n):
    name = input()
    players[name] = Player(name, n-i)
    
t = int(input())
for i in range(t):
    user, x, y = input().split()
    x = int(x)
    y = int(y)
    if (abs(x) + abs(y)) <= size:
        players[user].score += 15
        continue
    if x**2 + y**2 <= size**2:
        players[user].score += 10
        continue
    if abs(x) <= size and abs(y) <= size:
        players[user].score += 5
        continue

for each in sorted(players.values(), key=lambda x: (x.score, x.num), reverse=True):
    print(each)
    
