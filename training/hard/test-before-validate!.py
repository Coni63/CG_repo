import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
actions = []
actions_sorted = []
queue = []

n = int(input())
for i in range(n):
    actions.append(input())

print(actions, file=sys.stderr)
 
nb_orders = int(input())
for i in range(nb_orders):
    queue.append(input().split())
    
change = True
while change:
    change = False
    for each in queue:
        print("-------------", file=sys.stderr)
        a1, cond, a2 = each
        print(a1, cond, a2, file=sys.stderr)
        index_a1 = actions.index(a1)
        index_a2 = actions.index(a2)
        print(index_a1, index_a2, file=sys.stderr)
        if cond == "after" and index_a1-index_a2 != 1:
            actions.pop(index_a1)
            actions.insert(index_a2+1, a1)
            change = True
        elif cond == "before" and  index_a2-index_a1 != 1:
            actions.pop(index_a1)
            actions.insert(index_a2, a1)
            change = True
        print(actions, file=sys.stderr)
    
for each in actions:
    print(each)
    
"""    
while len(queue) > 0:
    a1, cond, a2 = queue.pop(0)
    if cond == "after":
        if a2 in actions_sorted and a1 not in actions_sorted:
            pos = actions_sorted.index(a2)+1
            actions_sorted.insert(pos, a1)
        elif a2 not in actions_sorted and a1 in actions_sorted:
            pos = actions_sorted.index(a1)
            actions_sorted.insert(pos, a2)
        elif actions_sorted == []:
            actions_sorted.append(a2)
            actions_sorted.append(a1)
        else:
            queue.append((a1, cond, a2))
    else:
        if a2 in actions_sorted and a1 not in actions_sorted:
            pos = actions_sorted.index(a2)
            actions_sorted.insert(pos, a1)
        elif a2 not in actions_sorted and a1 in actions_sorted:
            pos = actions_sorted.index(a1)+1
            actions_sorted.insert(pos, a2)
        elif actions_sorted == []:
            actions_sorted.append(a1)
            actions_sorted.append(a2)
        else:
            queue.append((a1, cond, a2))
    
for each in actions_sorted:
    print(each)
"""

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)


