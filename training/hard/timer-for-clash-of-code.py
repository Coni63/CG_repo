import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

game_start = 0
inp_arr = []
player = 1

n = int(input())

if n == 0:
    print("NO GAME")
else:
    for i in range(n):
        time_stamp = [int(x) for x in input().split(":")]
        step = time_stamp[0] * 60 + time_stamp[1]
        inp_arr.append(step)
    
    print(inp_arr, file=sys.stderr)
    
    if len(inp_arr) == 7:    
        game_start = inp_arr[-1]
    else:
        for i in range(len(inp_arr)):
            player_join = inp_arr[i]
            if player_join >= game_start:
                game_start = player_join - 256/(2**(i))
                player += 1
            
    game_start = max(game_start, 0)
        
    print(game_start, file=sys.stderr)
    
    print("{:d}:{:02d}".format(int(game_start//60), int(game_start%60)))   

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

