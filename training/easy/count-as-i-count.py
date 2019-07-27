import sys
import math

choices_P = {"P" + str(x) : x for x in range(1, 13)}
choices_num = {str(x) : x for x in range(2, 13)}

choices = {**choices_P, **choices_num}

c = 0
n = int(input())

q = [(n, [])]

while True:
    score, prev = q.pop(0)
    for move, gain in choices.items():
        if score + gain < 50 and len(prev) < 3:
            q.append((score + gain, prev + [move]))
        if score + gain == 50:
            c += 1
    if len(q) == 0:
        break

print(c)
