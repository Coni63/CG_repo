import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

rounds = int(input())
cash = int(input())
for i in range(rounds):
    play = input().split()
    
    bet = int(math.ceil(cash/4))
    cash -= bet
    
    if play[1] == "PLAIN":
        if play[2] == play[0]:
            cash += (35+1) * bet
    elif play[1] == "ODD":
        if int(play[0]) % 2 == 1:
            cash += (1+1)*bet
    else:
        if int(play[0]) % 2 == 0 and int(play[0]) != 0:
            cash += (1+1)*bet

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print(cash)
