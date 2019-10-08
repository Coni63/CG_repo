import sys
import math
import numpy as np
from scipy.spatial.distance import cdist
import time

# T -> Thor
# X -> Strike will hit here
# XXXXXXXXXXX
# XXXXXXXXXXX
# XXXXXXXXXXX
# XXXXXXXXXXX
# XXXXXXXXXXX
# XXXXXTXXXXX
# XXXXXXXXXXX
# XXXXXXXXXXX
# XXXXXXXXXXX
# XXXXXXXXXXX
# XXXXXXXXXXX

def norm_1(X, y):
    """
    https://fr.wikipedia.org/wiki/Distance_de_Manhattan
    Used to find the direction to go toward the center
    """
    return cdist(X, y, metric='cityblock')

def norm_inf(X, y):
    """
    https://fr.wikipedia.org/wiki/Distance_de_Tchebychev
    Used to compute the number of giants in the area
    """
    return cdist(X, y, metric='chebyshev')

def find_center(X):
    """
    Return center of a matrix of position
    Used ot get centroides of giants
    """
    C = np.mean(X, axis=0).astype(np.uint8)
    return np.expand_dims(C, axis=0)

def countInStrike(x, y):
    """
    Return the number of Giant in the lightning strike
    """
    dist = norm_inf(x, y)
    return (dist<=4).sum()

def countContact(x, y):
    """
    Return the number of Giant in contact next turn
    """
    dist = norm_inf(x, y)
    return (dist<=1).sum()

def getPosition(thor, move):
    """
    Return the position of Thor after a given move
    """
    if move in ["WAIT", "STRIKE"]:
        return thor
    
    tx, ty = thor[0]
    if move[0] == "N":
        ty -= 1
    elif move[0] == "S":
        ty += 1
    
    if move[-1] == "E":
        tx += 1
    elif move[-1] == "W":
        tx -= 1
    return np.array([[tx, ty]], dtype=np.uint8)
 
def find_move(thor, centerX, centerY):
    """
    Return the action to go closer to center of giants
    """
    tx, ty = thor[0]
    if (centerX > tx):
        if (centerY > ty):
            action = "SE"
        elif (centerY < ty):
            action = "NE"
        else:
            action = "E"
    elif (centerX < tx):
        if (centerY > ty):
            action = "SW"
        elif (centerY < ty):
            action = "NW"
        else:
            action = "W"
    else:
        if (centerY > ty):
            action = "S"
        elif (centerY < ty):
            action = "N"
        else:
            action = "WAIT"
    return action, getPosition(thor, action)
    
def escape(thor, ennemis):
    """
    Test all move and take the one maximizing number of giants in area and minimize distance to closest one
    """
    tx, ty = thor[0]
    options = []
    if tx < 39:
        futur_pos = getPosition(thor, "E")
        if (countContact(ennemis, futur_pos) == 0):
            options.append(["E", countInStrike(ennemis, futur_pos), futur_pos])

    if ty > 0:
        futur_pos = getPosition(thor, "N")
        if (countContact(ennemis, futur_pos) == 0):
            options.append(["N", countInStrike(ennemis, futur_pos), futur_pos])

    if (tx < 39) and (ty > 0):
        futur_pos = getPosition(thor, "NE")
        if (countContact(ennemis, futur_pos) == 0):
            options.append(["NE", countInStrike(ennemis, futur_pos), futur_pos])

    if (tx > 0) and (ty > 0):
        futur_pos = getPosition(thor, "NW")
        if (countContact(ennemis, futur_pos) == 0):
            options.append(["NW", countInStrike(ennemis, futur_pos), futur_pos])

    if ty < 17:
        futur_pos = getPosition(thor, "S")
        if (countContact(ennemis, futur_pos) == 0):
            options.append(["S", countInStrike(ennemis, futur_pos), futur_pos])

    if (tx < 39) and (ty < 17):
        futur_pos = getPosition(thor, "SE")
        if (countContact(ennemis, futur_pos) == 0):
            options.append(["SE", countInStrike(ennemis, futur_pos), futur_pos])

    if (tx > 0) and (ty > 0):
        futur_pos = getPosition(thor, "SW")
        if (countContact(ennemis, futur_pos) == 0):
            options.append(["SW", countInStrike(ennemis, futur_pos), futur_pos])

    if tx > 0:
        futur_pos = getPosition(thor, "W")
        if (countContact(ennemis, futur_pos) == 0):
            options.append(["W", countInStrike(ennemis, futur_pos), futur_pos])

    bestOption = ["STRIKE", 0, thor, 0]
    bestDist = 0
    center = find_center(ennemis)
    for direction, inrange, next_pos in options:
        dist = norm_1(next_pos, center)
        if ((inrange > bestOption[1]) or ((inrange == bestOption[1]) and (dist > bestOption[3]))):
            bestOption = [direction, inrange, next_pos, dist]
    return bestOption[0], bestOption[2]
    
def findBestMove(thor, ennemis):
    """
    Decide the smartest move based on Than and Giants position
    """
    centerX, centerY = find_center(ennemis)[0]
    if (countContact(thor, ennemis) == 0):
        direction, next_pos = find_move(thor, centerX, centerY)
    else:
        direction, next_pos = escape(thor, ennemis)
    return direction, next_pos

def move(thor, ennemis):
    """
    Makes the move and return the new position of Thor
    """
    closest_giants = countInStrike(ennemis, thor)
    if ennemis.shape[0] == closest_giants:
        action, next_pos = "STRIKE", thor
    else:
        action, next_pos = findBestMove(thor, ennemis)  
    return action, next_pos

thor = np.array([[int(i) for i in input().split()]], dtype=np.uint8)

# game loop
while True:
    # h: the remaining number of hammer strikes.
    # n: the number of giants which are still present on the map.
    h, n = [int(i) for i in input().split()]
    ennemis = np.zeros(shape=(n, 2))
    for i in range(n):
        ennemis[i] = [int(j) for j in input().split()]
    
    tic = time.time()
    action, thor = move(thor, ennemis)
    toc = time.time()
    print(action)
    
    print(toc-tic, file=sys.stderr)

    # The movement or action to be carried out: WAIT STRIKE N NE E SE S SW W or N
