import sys
import math
from collections import defaultdict


reverse = {"RIGTH":"LEFT", "LEFT":"RIGHT"}

def BFS(world, start_x, exit_floor, remaining_elevators, nb_rounds):
    """
    a state will be structure as a dict with:
    path : []
    pos_x : int
    level : int
    length : int
    remaining_elevators : int    
    """
    states = [{
        "path" : [],
        "pos_x" : start_x,
        "level" : 0,
        "length" : 0,
        "remaining_elevators" : remaining_elevators,
        "direction" : "RIGHT"
        }]
    while True:
        if states[0]["level"] == exit_floor:
            return states
        
        current_state = states.pop(0)
        
        if current_state["length"] > nb_rounds:
            continue
                
        if len( world[current_state["level"]] ) == 0:  # if there is no elevator
            if current_state["remaining_elevators"] > 0:
                states.append({
                    "path" : current_state["path"] + ["ELEVATOR"],
                    "pos_x" : current_state["pos_x"],
                    "level" : current_state["level"] + 1,
                    "length" : current_state["length"] + 1,
                    "remaining_elevators" : current_state["remaining_elevators"] - 1,
                    "direction" : current_state["direction"]
                })
            else:
                continue # remove the element
        else:
            left_x = 1e6
            right_x = 1e6
            elevator_right_x = 1e6
            elevator_left_x = 1e6
            for elevator_x in world[current_state["level"]]:
                if elevator_x > current_state["pos_x"]: # if right
                    delta_x =  elevator_x-current_state["pos_x"]
                    if delta_x < right_x:
                        right_x = delta_x
                        elevator_right_x = elevator_x
                elif elevator_x < current_state["pos_x"]:
                    delta_x = current_state["pos_x"]-elevator_x
                    if delta_x < left_x:
                        left_x = delta_x
                        elevator_left_x = elevator_x
                elif elevator_x == current_state["pos_x"]:
                    states.append({
                        "path" : current_state["path"] + ["WAIT"],
                        "pos_x" : current_state["pos_x"],
                        "level" : current_state["level"] + 1,
                        "length" : current_state["length"] + 1,
                        "remaining_elevators" : current_state["remaining_elevators"],
                        "direction" : current_state["direction"]
                    })
                    
                    

            if elevator_right_x < 101:
                if current_state["direction"] != "RIGHT":
                    offset = 2
                else:
                    offset = 0
                states.append({
                    "path" : current_state["path"] + ["RIGHT"],
                    "pos_x" : elevator_right_x,
                    "level" : current_state["level"] + 1,
                    "length" : current_state["length"] + right_x + offset,
                    "remaining_elevators" : current_state["remaining_elevators"],
                    "direction" :"RIGHT"
                })
            if 0 < elevator_left_x < 101:
                if current_state["direction"] != "LEFT":
                    offset = 2
                else:
                    offset = 0
                states.append({
                    "path" : current_state["path"] + ["LEFT"],
                    "pos_x" : elevator_left_x,
                    "level" : current_state["level"] + 1,
                    "length" : current_state["length"] + left_x + offset,
                    "remaining_elevators" : current_state["remaining_elevators"],
                    "direction" :"LEFT"
                })
            if current_state["remaining_elevators"] > 0:
                states.append({
                    "path" : current_state["path"] + ["ELEVATOR"],
                    "pos_x" : current_state["pos_x"],
                    "level" : current_state["level"] + 1,
                    "length" : current_state["length"] + 1,
                    "remaining_elevators" : current_state["remaining_elevators"] - 1,
                    "direction" : current_state["direction"]
                })
        



maze = defaultdict(list)

# nb_floors: number of floors
# width: width of the area
# nb_rounds: maximum number of rounds
# exit_floor: floor on which the exit is found
# exit_pos: position of the exit on its floor
# nb_total_clones: number of generated clones
# nb_additional_elevators: number of additional elevators that you can build
# nb_elevators: number of elevators
nb_floors, width, nb_rounds, exit_floor, exit_pos, nb_total_clones, nb_additional_elevators, nb_elevators = [int(i) for i in input().split()]
for i in range(nb_elevators):
    # elevator_floor: floor on which this elevator is found
    # elevator_pos: position of the elevator on its floor
    elevator_floor, elevator_pos = [int(j) for j in input().split()]
    maze[elevator_floor].append(elevator_pos)

print(nb_additional_elevators, file=sys.stderr)

loop = 0

# game loop
while True:
    # clone_floor: floor of the leading clone
    # clone_pos: position of the leading clone on its floor
    # direction: direction of the leading clone: LEFT or RIGHT
    clone_floor, clone_pos, direction = input().split()
    clone_floor = int(clone_floor)
    clone_pos = int(clone_pos)
    
    if loop == 0:
        states = BFS(maze, clone_pos, exit_floor, nb_additional_elevators, nb_rounds)
        shortest = 1e6
        for state in states:
            print(state["length"], file=sys.stderr)
            print(state["path"], file=sys.stderr)
            if state["length"] < shortest:
                shortest = state["length"]
                path = state["path"]
    
    print(path, file=sys.stderr)
        
    loop += 1
    
    # Handle turn with no clone 
    if direction == "NONE":
        print("WAIT")
        continue
    
    # handle last floor
    if clone_floor == exit_floor:
        if exit_pos > clone_pos and direction == "RIGHT":
            print("WAIT")
        elif exit_pos < clone_pos and direction == "LEFT":
            print("WAIT")
        else:
            print("BLOCK")
        continue
            
    # handle best paths
    if path[clone_floor] == "ELEVATOR":
        path[clone_floor] = "WAIT"
        print("ELEVATOR")
    elif path[clone_floor] == "WAIT":
        print("WAIT")
    elif path[clone_floor] != direction:
        print("BLOCK")
    else:
        print("WAIT")
    
    
    
