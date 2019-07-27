import sys
import math
import copy

reverse = {"LEFT":"RIGHT", "RIGHT":"LEFT", "UP":"DOWN", "DOWN":"UP", None: None}
change_dir = {"LEFT":"DOWN", "RIGHT":"UP", "UP":"LEFT", "DOWN":"RIGHT"}
choice = {"UP":["UP","RIGHT","LEFT"],"DOWN":["DOWN","RIGHT","LEFT"],"RIGHT":["RIGHT","DOWN","UP"],"LEFT":["LEFT","DOWN","UP"]}

UNKNOWN = '?'
PART_OF_PATH = '.'
TRIED = 'o'
OBSTACLE = '#'
DEAD_END = '-'
START = 'T'
END = 'C' 
RETURN = 'X'

class Maze():
    def __init__(self, _map):
        self.maze = _map
        self.start = []
        self.end = []
        self.kirk_pos = []
        self.status = 0  # 0 = Explo, 1 = Return
        self.distance = 0
        self.actions = []
    
    def update(self, row, idx):
        for col in range(c):
            if self.maze[idx][col] == UNKNOWN and row[col] != UNKNOWN:
                self.maze[idx][col] = row[col]
            if row[col] == END and self.end == []:
                self.end = [idx, col]
                
    def show(self):
        for each in self.maze:
            print("".join(each), file=sys.stderr)

    def evaluate_direction(self, direction):
        view = self.look(direction)
        if view not in [OBSTACLE, TRIED]:
            return 1
        elif view == TRIED:
            return 2
        return 0

    def look(self, direction):
        if direction == "UP":
            return self.maze[self.kirk_pos[0] - 1][self.kirk_pos[1]]
        elif direction == "DOWN":
            return self.maze[self.kirk_pos[0] + 1][self.kirk_pos[1]]
        elif direction == "RIGHT":
            return self.maze[self.kirk_pos[0]][self.kirk_pos[1] + 1]
        elif direction == "LEFT":
            return self.maze[self.kirk_pos[0]][self.kirk_pos[1] - 1]

    def compute_distance(self, pts):
        # manhattan distance from start (to be maximize)
        dx = abs(pts[1] - self.start[1])
        dy = abs(pts[0] - self.start[0])
        s = dx + dy
        if self.status == 0:
            if self.maze[self.kirk_pos[0]][self.kirk_pos[1]] == TRIED:
                s //2
        return s

    def simulate(self, direction):
        if direction == "UP":
            new_position = [self.kirk_pos[0] - 1, self.kirk_pos[1]]
        elif direction == "DOWN":
            new_position = [self.kirk_pos[0] + 1, self.kirk_pos[1]]
        elif direction == "RIGHT":
            new_position = [self.kirk_pos[0], self.kirk_pos[1] + 1]
        elif direction == "LEFT":
            new_position = [self.kirk_pos[0], self.kirk_pos[1] - 1]
        self.distance = self.compute_distance(new_position)
        self.kirk_pos = new_position
        self.maze[self.kirk_pos[0]][self.kirk_pos[1]] = TRIED
        self.actions.append(direction)

    def mark(self, status):
        y = self.kirk_pos[0]
        x = self.kirk_pos[1]
        self.maze[y][x] = status


# r, c: number of rows / columns.
# a: number of rounds between the time the alarm countdown is activated and the time the alarm goes off.
r, c, a = [int(i) for i in input().split()]

grid = [["?" for _ in range(c)] for _ in range(r)]
maze = Maze(grid)

actions = ["UP", "RIGHT", "LEFT", "DOWN"]

while True:# and step < 100:
    # kr, kc: row, column where Kirk is located.
    kr, kc = [int(i) for i in input().split()]
    maze.kirk_pos=[kr, kc]
    if maze.kirk_pos == maze.end:
        print("top", file=sys.stderr)
        status == 1

    if len(maze.start) == 0:
        maze.start = [kr, kc]
    
    for i in range(r):
        row = list(input())  # C of the characters in '#.TC?' (i.e. one line of the ASCII maze).
        maze.update(row, i)

    maze.show()

    if maze.status ==0:
        main_queue = []
        second_queue = []
        for action in actions:
            result = maze.evaluate_direction(action)
            if result == 1:
                main_queue.append(action)
            elif result == 2:
                second_queue.append(action)
        if len(main_queue) == 0:
            selected_action = second_queue[0]
            maze.mark(OBSTACLE)
        elif len(main_queue) >= 1:
            selected_action = main_queue[0]
            maze.mark(TRIED)
        print(selected_action)
    else:
        pass



