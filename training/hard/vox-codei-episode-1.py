import sys
import math


class Grid:
    def __init__(self, W, H):
        self.height = H
        self.width = W
        self.arr = []

    def show(self):
        for line in self.arr:
            print(list(map(str, line)), file=sys.stderr)
            
    def evaluate(self, pos):
        x,y = pos
        bomb_touched = 0
        ### Vertical up check
        for i in range(1,4):
            if y-i >= 0:
                if self.arr[y-i][x] == "#":
                    break # fin du for
                elif self.arr[y-i][x] == "@":
                    bomb_touched += 1
                else:
                    pass
        
        ### Vertical down check
        for i in range(1,4):
            if y+i < height:
                if self.arr[y+i][x] == "#":
                    break # fin du for
                elif self.arr[y+i][x] == "@":
                    bomb_touched += 1
                else:
                    pass
        
        ### Horizontal right check
        for i in range(1,4):
            if x-i >= 0:
                if self.arr[y][x-i] == "#":
                    break # fin du for
                elif self.arr[y][x-i] == "@":
                    bomb_touched += 1
                else:
                    pass
        
        ### Horizontal left check
        for i in range(1,4):
            if x+i < width:
                if self.arr[y][x+i] == "#":
                    break # fin du for
                elif self.arr[y][x+i] == "@":
                    bomb_touched += 1
                else:
                    pass
        
        return bomb_touched
    
    def update(self, pos):
        x,y = pos
        self.arr[y][x] = "B"
        ### Vertical up check
        for i in range(1,4):
            if y-i >= 0:
                if self.arr[y-i][x] == "#":
                    break # fin du for
                elif self.arr[y-i][x] == "@":
                    self.arr[y-i][x] = 3
                else:
                    pass
        
        ### Vertical down check
        for i in range(1,4):
            if y+i < height:
                if self.arr[y+i][x] == "#":
                    break # fin du for
                elif self.arr[y+i][x] == "@":
                    self.arr[y+i][x] = 3
                else:
                    pass
        
        ### Horizontal right check
        for i in range(1,4):
            if x-i >= 0:
                if self.arr[y][x-i] == "#":
                    break # fin du for
                elif self.arr[y][x-i] == "@":
                    self.arr[y][x-i] = 3
                else:
                    pass
        
        ### Horizontal left check
        for i in range(1,4):
            if x+i < width:
                if self.arr[y][x+i] == "#":
                    break # fin du for
                elif self.arr[y][x+i] == "@":
                    self.arr[y][x+i] = 3
                else:
                    pass
                
    def tick(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.arr[y][x] in [1, 2, 3]:
                    self.arr[y][x] -= 1
                    if self.arr[y][x] == 0:
                        self.arr[y][x] = '.'
    
    def count_bomb(self):
        return sum([x.count("@") for x in self.arr])
            
    
    """
    def is_symetric(self):
        flag = True
        
        for y in range(self.height):
            for x in range(self.width // 2):
                if self.arr[y][x] != self.arr[y][-x-1]:
                    flag = False
        
        for x in range(self.width):
            for y in range(self.height // 2):
                print(self.arr[y][x], self.arr[-y-1][x], file=sys.stderr)
                if self.arr[y][x] != self.arr[-y-1][x]:
                    flag = False

        return flag
    """
    
    def is_symetric(self):
        list_x = []
        list_y = []
        for y in range(self.height):
            for x in range(self.width):
                if self.arr[y][x] == "@":
                    list_x.append(x)
                    list_y.append(y)
        if len(list_x)>1:
            avg_x = sum(list_x)/len(list_x)
            avg_y = sum(list_y)/len(list_y)
            if avg_x.is_integer() and avg_y.is_integer():
                self.arr[int(avg_y)][int(avg_x)] = 'X'


width, height = [int(i) for i in input().split()]
grid = Grid(width, height)

for i in range(height):
    grid.arr.append(list(input()))  # one line of the firewall grid

grid.is_symetric()

total_bomb = grid.count_bomb()
#print(sym, total_bomb, file=sys.stderr)

grid.show()

init_bomb = None
target = 30

while True:
    bomb_destroyed_at_best_pos = 0
    best_pos = None
    rounds, bombs = [int(i) for i in input().split()]
    if init_bomb is None:
        init_bomb = bombs
    #    target = total_bomb // init_bomb
            
    if bombs == 0:
        print("WAIT")
    elif bombs > 1:
        for x in range(width):
            for y in range(height):
                position = (x, y)
                if grid.arr[y][x] == ".":
                    bomb_destroyed = grid.evaluate(position)
                    #print(position, bomb_destroyed, file=sys.stderr)
                    if bomb_destroyed > bomb_destroyed_at_best_pos :
                        bomb_destroyed_at_best_pos = bomb_destroyed
                        best_pos = position
        if best_pos is not None:
            grid.update(best_pos)
            grid.show()
            print(best_pos[0], best_pos[1])
        else:
            print("WAIT")
        grid.tick()             
    else:
        if rounds > 4:
            print("WAIT")
            grid.tick()   
        else:
            for x in range(width):
                for y in range(height):
                    position = (x, y)
                    if grid.arr[y][x] == "." or (init_bomb == 1 and grid.arr[y][x] in [".", "X"]):
                        bomb_destroyed = grid.evaluate(position)
                        #print(position, bomb_destroyed, file=sys.stderr)
                        if bomb_destroyed > bomb_destroyed_at_best_pos:
                            bomb_destroyed_at_best_pos = bomb_destroyed
                            best_pos = position
                            
            if best_pos is not None:
                grid.update(best_pos)
                grid.show()
                print(best_pos[0], best_pos[1])
            grid.tick()  
        
