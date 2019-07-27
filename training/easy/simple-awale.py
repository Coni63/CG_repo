import sys
import math

op_bowls = [int(x) for x in input().split()]
my_bowls = [int(x) for x in input().split()]
num = int(input())

my_hand = my_bowls[num]
my_bowls[num] = 0

side = "mine"
index = num + 1
replay = False

for _ in range(my_hand):
    if side == "mine" and index < 6:
        my_bowls[index] += 1 
        index += 1
        replay = False
    elif side == "mine" and index == 6:
        my_bowls[index] += 1 
        index = 0
        side = "yours"
        replay = True
    elif side == "yours" and index < 5:
        op_bowls[index] += 1 
        index += 1
        replay = False
    else:
        op_bowls[index] += 1 
        index = 0
        side = "mine"
        replay = False


my_bowls = [str(x) for x in my_bowls]
op_bowls = [str(x) for x in op_bowls]

my_bowls[-1] = "[" +my_bowls[-1]+ "]"
op_bowls[-1] = "[" +op_bowls[-1]+ "]"

print(" ".join(op_bowls))
print(" ".join(my_bowls))

if replay:
    print("REPLAY")
