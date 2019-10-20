import sys
import math
import time
             
class aDallas():
    def __init__(self, X0, Y0):
        self.row = Y0
        self.col = X0
        self.previous_row = Y0
        self.previous_col = X0
        self.available_rows = list(range(h))
        self.available_cols = list(range(w))
        self.reduce_cols = (w > 1)  # start by reducing cols first
        self.visited_rows = set()
    
    def jump(self, row, col):
        print(col, row)  # this puzzle uses x, y insteaf of row, col
        # print(self.available_rows, file=sys.stderr)
        # print(self.available_cols, file=sys.stderr)
        self.previous_row, self.row = self.row, row
        self.previous_col, self.col = self.col, col
        if not self.reduce_cols:
            self.visited_rows.add(row)
    
    def move(self, direction):
        # print(self.previous_row, self.previous_col, "->", self.row, self.col, direction, file=sys.stderr)
        
        self.update_possible_positions(direction)
        
        if len(self.available_cols) == 1:
            self.reduce_cols = False
        
        if len(self.available_cols)==1 and self.available_cols[0]!=self.col:
            next_col=self.available_cols[0]
            self.jump(self.row, next_col)
            return True
        
        if len(self.available_rows)==1 and self.available_rows[0]!=self.row:
            next_row=self.available_rows[0]
            self.jump(next_row, self.col)
            return True
        
        if len(self.available_cols)>1:
            next_col = self.dichotomie()
            next_row = self.row
        else:
            next_col = self.col
            next_row = self.dichotomie()
        self.jump(next_row, next_col)

    def update_possible_positions(self, direction):
        if direction == 'SAME':
            if self.col != self.previous_col:
                self.available_cols = [(self.previous_col+self.col)//2]
            else:
                self.available_rows = [(self.previous_row+self.row)//2]
        elif direction == 'WARMER':
            if self.col != self.previous_col:
                self.available_cols = [x for x in self.available_cols if abs(x-self.col)<abs(x-self.previous_col)]
            else:
                self.available_rows = [x for x in self.available_rows if abs(x-self.row)<abs(x-self.previous_row)]
        elif direction == 'COLDER':
            if self.col != self.previous_col:
                self.available_cols = [x for x in self.available_cols if abs(x-self.col)>abs(x-self.previous_col)]
            else:
                self.available_rows = [x for x in self.available_rows if abs(x-self.row)>abs(x-self.previous_row)]
 
    def dichotomie(self):
        if self.reduce_cols:
            a = self.col
            mirror = self.available_cols[0] + self.available_cols[-1] - a
            limit = w-1
        else:
            a = self.row
            mirror = self.available_rows[0] + self.available_rows[-1] - a
            limit = h-1
        
        mirror += 1 * (mirror == a)
            
        mirror = min(max(mirror,0), limit)

        if a==0 or a==limit:
            mirror = (mirror+a)//2
            if mirror==0:
                mirror=1
            elif mirror==limit:
                mirror -= 1

        ### With this activated, the bomb position changes and cannot be solved with 3 steps
        # if mirror > limit//2:
        #     while mirror in self.visited_rows:
        #         mirror -= 1
        # else:
        #     while mirror in self.visited_rows:
        #         mirror += 1
                
        return mirror
           
# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]

n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]
batman = aDallas(x0, y0)

# game loop
while True:
    bomb_dir = input()  # Current distance to the bomb compared to previous distance (COLDER, WARMER, SAME or UNKNOWN)
    start = time.time()
    batman.move(bomb_dir)
    stop = time.time()
    print(stop-start, file=sys.stderr)
