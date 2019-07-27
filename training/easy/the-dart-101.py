import sys
import math

def get_score(x):
    while len(x) > 0:
        v = x.pop(0)
        if v == "X":
            yield v
        elif v.count("*") > 0:
            a, b = v.split("*")
            yield int(a) * int(b)
        else:
            yield int(v)

def get_round(gen):
    turn = 1
    score = 0
    missed_cons = 0
    missed_total = 0
    loop = 0
    for i, v in enumerate(gen):
        if v == "X":
            missed_cons += 1
            missed_total += 1
            if missed_total == 3:
                score = 0
            elif missed_cons == 1:
                score = max(0, score-20)
            elif missed_cons == 2:
                score = max(0, score-30)
        else:
            score += v
            missed_cons = 0
            if score > 101 : 
                score -= v
                turn += 1
                missed_total = 0
                loop = 0
                continue
        
        if loop == 2:
            turn += 1
            missed_cons = 0
            missed_total = 0
            loop = 0
            continue
        
        loop += 1

        if score == 101:
            return turn, 101
    return 1000, score


status = []

n = int(input())
for i in range(n):
    player = input()
    status.append([player, 1000, 0])
    
for i in range(n):
    shots = input().split()
    generator = get_score(shots)
    turn, score = get_round(generator)
    status[i][1] = turn
    status[i][2] = -score

print(status, file=sys.stderr)

status = sorted(status, key = lambda x: (x[1], x[2]))
print(status[0][0])
