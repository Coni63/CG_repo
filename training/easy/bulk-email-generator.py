import sys
import math
import re

n = int(input())
txt = ";".join([input() for i in range(n)])

groups = re.findall(r'(\([^\)]+\))', txt)

to_use = []
for i, group in enumerate(groups):
    subgroup = group[1:-1].split("|")
    picked = subgroup[i%len(subgroup)]
    to_use.append(picked)

for res in to_use:
    txt = re.sub(r'(\([^\)]+\))', res, txt, 1)

for each in txt.split(";"):
    print(each)

