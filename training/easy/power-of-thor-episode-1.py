import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]

thor_x = initial_tx
thor_y = initial_ty

# game loop
while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.

    go_to_E = light_x-thor_x
    go_to_S = light_y-thor_y
    
    if math.fabs(go_to_E) == math.fabs(go_to_S):
        if light_x > thor_x and light_y > thor_y:
            print("SE")
            thor_x+=1
            thor_y+=1
        elif light_x > thor_x and light_y < thor_y:
            print("NE")
            thor_x+=1
            thor_y-=1
        elif light_x < thor_x and light_y > thor_y:
            print("SW")
            thor_x-=1
            thor_y+=1
        elif light_x < thor_x and light_y < thor_y:
            print("NW")
            thor_x-=1
            thor_y-=1
    if math.fabs(go_to_E) > math.fabs(go_to_S):
        if go_to_E > 0 :
            print("E")
            thor_x+=1
        else:
            print("W")
            thor_x-=1
            
    if math.fabs(go_to_E) < math.fabs(go_to_S):
        if go_to_S > 0:
            print("S")
            thor_y+=1
        else:
            print("N")
            thor_y-=1
    
     
    # To debug: print("Debug messages...", file=sys.stderr)


