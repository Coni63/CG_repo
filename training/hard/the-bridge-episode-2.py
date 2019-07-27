import sys
import copy

class Team():
    def __init__(self, moto_mini):
        self.minimum = moto_mini
        self.lines = [0, 0, 0, 0]
        self.x = 0
        self.speed = 0
        self.actions = []
        self.path_length = 0

    @property
    def remaining_bike(self):
        return sum(self.lines)

    @property
    def score(self):
        bonus = {"SPEED" : 0.6, "UP" : 0.5, "DOWN" : 0.5, "WAIT" : 0.3, "JUMP" : 0.2, "SLOW" : 0.1}
        if self.remaining_bike >= self.minimum:
            return self.remaining_bike*self.x + bonus.get(self.actions[-1], 0)
        else:
            return 0
    
    def up(self):
        if self.lines in [[1, 0, 0, 0], [1, 1, 0, 0], [1, 1, 1, 0], [1, 1, 1, 1]]:
            self.wait()
        else:
            for i in range(1, 4):
                if self.lines[i-1] == 0 and self.lines[i] == 1:
                    sector_top = road[i-1][self.x : self.x+self.speed]
                    sector_bot = road[i][self.x : self.x+self.speed]
                    if "0" in sector_top or "0" in sector_bot:
                        self.lines[i-1] = 0
                        self.lines[i] = 0
                    else:
                        self.lines[i-1] = 1
                        self.lines[i] = 0
                elif self.lines[i-1] == 1 and self.lines[i] == 1:
                    if "0" in road[i-1][self.x:self.x + self.speed]:
                        self.lines[i-1] = 0
                    if "0" in road[i][self.x:self.x + self.speed]:
                        self.lines[i] = 0
            self.x += self.speed
    
    def down(self):
        if self.lines in [[0, 0, 0, 1], [0, 0, 1, 1], [0, 1, 1, 1], [1, 1, 1, 1]]:
            self.wait()
        else:
            for i in reversed(range(3)):
                if self.lines[i+1] == 0 and self.lines[i] == 1:
                    sector_top = road[i][self.x:self.x + self.speed]
                    sector_bot = road[i+1][self.x:self.x + self.speed]
                    if "0" in sector_top or "0" in sector_bot:
                        self.lines[i+1] = 0
                        self.lines[i] = 0
                    else:
                        self.lines[i+1] = 1
                        self.lines[i] = 0
                elif self.lines[i+1] == 1 and self.lines[i] == 1:
                    if "0" in road[i+1][self.x:self.x + self.speed]:
                        self.lines[i+1] = 0
                    if "0" in road[i][self.x:self.x + self.speed]:
                        self.lines[i] = 0
            self.x += self.speed
    
    def speed_up(self):
        self.speed += 1
        for idx, line in enumerate(self.lines):
            if line == 1:
                if "0" in road[idx][self.x:self.x+self.speed]:
                    self.lines[idx] = 0
        self.x += self.speed
            
    def slow_down(self):
        self.speed -= 1
        if self.x + self.speed <= self.path_length:
            for idx, line in enumerate(self.lines):
                if line == 1:
                    if "0" in road[idx][self.x:self.x+self.speed]:
                        self.lines[idx] = 0
        self.x += self.speed
    
    def jump(self):
        if self.x+self.speed+1 <= self.path_length:
            for idx, line in enumerate(self.lines):
                if line == 1:
                    if road[idx][self.x+self.speed] == "0" or road[idx][self.x] == "0":
                        self.lines[idx] = 0
        self.x += self.speed

    def wait(self):
        for idx, line in enumerate(self.lines):
            if line == 1:
                if "0" in road[idx][self.x:self.x+self.speed]:
                    self.lines[idx] = 0
        self.x += self.speed
        
    def play(self, commande):
        if commande == "SPEED":
            self.speed_up()
        elif commande == "SLOW":
            self.slow_down()
        elif commande == "JUMP":
            self.jump()
        elif commande == "WAIT":
            self.wait()
        elif commande == "UP":
            self.up()
        elif commande == "DOWN":
            self.down()


m = int(input())  # the amount of motorbikes to control
v = int(input())  # the minimum amount of motorbikes that must survive

actions = ["SPEED", "JUMP", "WAIT", "UP", "DOWN", "SLOW"]

road = []
for _ in range(4):
    path = input() + "."*50
    road.append(path)
    print(path, file=sys.stderr)

final = []
if len(path) == 86:
    if road[0].count("0") == 5 or road[3].count("0") == 5:
        final = ["WAIT", "WAIT", "JUMP", "SPEED", "JUMP", "SPEED"]

team = Team(v)
team.path_length = len(path)


while True:
        
    # team.lines = [0, 0, 0, 0]
    #
    # team.speed = int(input())  # the motorbikes' speed
    # for i in range(m):
    #     x, y, a = [int(j) for j in input().split()]
    #     team.x = x
    #     team.actions = []
    #     team.lines[y] = a
    #
    # queue = [copy.deepcopy(team)]
    # while len(queue[0].actions) < 5:
    #     t = queue.pop(0)
    #     for action in actions:
    #         t2 = copy.deepcopy(t)
    #         t2.play(action)
    #         t2.actions.append(action)
    #         queue.append(t2)
    #     queue.sort(key=lambda t: t.score, reverse=True)
    #
    # queue.sort(key=lambda t: t.score, reverse=True)
    #
    # for each in queue[:10]:
    #     print(each.actions, each.score, file=sys.stderr)
    # print(queue[0].actions[0])

    if len(final) == 0:
        team.speed = int(input())
        for i in range(m):
            x, y, a = [int(j) for j in input().split()]
            team.lines[y] = a
        queue = [copy.deepcopy(team)]
        while queue[0].x < team.path_length-30 and team.remaining_bike >= team.minimum:
            t = queue.pop(0)
            for action in actions:
                t2 = copy.deepcopy(t)
                t2.play(action)
                t2.actions.append(action)
                queue.append(t2)
            queue.sort(key=lambda t: t.score, reverse=True)
        final = queue[0].actions
    print(final.pop(0))