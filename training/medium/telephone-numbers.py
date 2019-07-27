import sys
import math
    
tree = {}

n = int(input())
listing = [input() for _ in range(n)]

for each_word in listing:
    for i in range(1,len(each_word)+1):
        if each_word[:i] not in tree.keys():
            tree[each_word[:i]] = 1

print(len(tree.keys()))
    
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
