import sys
import math

class State:
    def __init__(self, x, y, action, parent):
        self.x = x
        self.y = y
        self.action = action
        self.parent = parent
        self.block_ID = arr[self.y][self.x]
        self.outcome = []
        self.to_delete = False

    def valid_block(self, side_in):
        if type_block[self.block_ID].get(side_in, None) is not None:
            return True
        else:
            return False

    def simulate(self, side_in):
        for action in self.action:
            if action == "NONE":
                pass
            else:
                self.block_ID = rotate[action][self.block_ID]

        if not self.valid_block(side_in):
            return -1
        else:
            side_out = type_block[self.block_ID][side_in]
            if side_out == "BOTTOM":
                x, y = self.x, self.y + 1
            elif side_out == "LEFT":
                x, y = self.x - 1, self.y
            elif side_out == "RIGHT":
                x, y = self.x + 1, self.y
            side_in = invert[side_out]
            self.outcome = [x, y, side_in]
            return self.outcome


type_block = {  0:{"BLOCK":"BLOCK"}, 
                1:{"RIGHT":"BOTTOM", "LEFT":"BOTTOM", "TOP":"BOTTOM"},
                2:{"RIGHT":"LEFT", "LEFT":"RIGHT"}, 
                3:{"TOP":"BOTTOM"}, 
                4:{"TOP":"LEFT", "RIGHT":"BOTTOM"}, 
                5:{"TOP":"RIGHT", "LEFT":"BOTTOM"}, 
                6:{"RIGHT":"LEFT", "LEFT":"RIGHT"}, 
                7:{"RIGHT":"BOTTOM", "TOP":"BOTTOM"}, 
                8:{"RIGHT":"BOTTOM", "LEFT":"BOTTOM"}, 
                9:{"LEFT":"BOTTOM", "TOP":"BOTTOM"}, 
                10:{"TOP":"LEFT"}, 
                11:{"TOP":"RIGHT"}, 
                12:{"RIGHT":"BOTTOM"}, 
                13:{"LEFT":"BOTTOM"}
            }

rotate = { "RIGHT" : {1:1, 2:3, 3:2, 4:5, 5:4, 6:7, 7:8, 8:9, 9:6, 10:11, 11:12, 12:13, 13:10},
            "LEFT" : {1:1, 2:3, 3:2, 4:5, 5:4, 6:9, 9:8, 8:7, 7:6, 10:13, 13:12, 12:11, 11:10} }

invert = {"RIGHT":"LEFT", "LEFT":"RIGHT", "BOTTOM":"TOP"}

actions = [["NONE"], ["RIGHT"], ["LEFT"], ["LEFT", "LEFT"]]

def next_node(x, y, side_in):
    while arr[y][x] < 0:
        block = arr[y][x]
        side_out = type_block[abs(block)][side_in]

        if side_out == "BOTTOM":
            x, y = x, y+1
        elif side_out == "LEFT":
            x, y = x-1, y
        elif side_out == "RIGHT":
            x, y = x+1, y

        side_in = invert[side_out]
    return x, y, side_in


arr = []
# w: number of columns.
# h: number of rows.
w, h = [int(i) for i in input().split()]
for i in range(h):
    line = input()  # each line represents a line in the grid and contains W integers T. The absolute value of T specifies the type of the room. If T is negative, the room cannot be rotated.
    arr.append([int(x) for x in line.split()])
    # print(line, file=sys.stderr)
ex = int(input())  # the coordinate along the X axis of the exit.

state_list = []

# game loop
while True:
    xi, yi, side_in = input().split()
    xi = int(xi)
    yi = int(yi)
    r = int(input())  # the number of rocks currently in the grid.
    for i in range(r):
        xr, yr, posr = input().split()
        xr = int(xr)
        yr = int(yr)

    for i in range(3):
        if len(state_list) == 0:
            parent = None
            x, y, side_in = next_node(xi, yi, side_in)
        else:
            parent = state_list.pop(0)
            x, y, side_in = parent.outcome

        for action in actions:
            s = State(x, y, action, parent)
            expected_state = s.simulate(side_in)
            if expected_state == -1:
                pass
            else:
                x, y, side_in = expected_state
                x, y, side_in = next_node(x, y, side_in)
                state_list.append(s)

        print(state_list, file=sys.stderr)
    print("WAIT")





    # if next_block > 0:
    #     if check_orientation(in_direction, next_block, "NONE"): #si on peut sortir sans tourner
    #         print("WAIT")
    #     elif check_orientation(in_direction, next_block,"RIGHT"): #sinon on verifie en tournant a droite
    #         rotate_block(next_pos, "RIGHT")
    #     elif check_orientation(in_direction, next_block, "LEFT"): #ou a gauche
    #         rotate_block(next_pos, "LEFT")
    # else:
    #     print("WAIT")

