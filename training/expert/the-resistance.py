import sys
import math
import time

class TreeNode:
    def __init__(self):
        self.parent = None
        self.dotChild = None
        self.dashChild = None
        self.valid = 0

def encode(word):
    encoded = ""
    for each in word:
        encoded += morseAlphabet[each]
    return encoded
    
def insert(node, code, pos = 0):
    for char in code:
        if char == ".":
            if node.dotChild is None:
                node.dotChild = TreeNode()
            node = node.dotChild
        else:
            if node.dashChild is None:
                node.dashChild = TreeNode()
            node = node.dashChild
    node.valid += 1
    
def solve(pos, node):
    result = 0
    while pos < len(l):
        char = l[pos]
        if (char == ".") and (node.dotChild is not None):
            node = node.dotChild
        elif (char == "-") and (node.dashChild is not None):
            node = node.dashChild
        else:
            break
        
        if node.valid > 0:
            if pos == len(l)-1:
                result += node.valid
            else:
                if cache.get(pos+1, False):
                    result += cache[pos+1] * node.valid
                else:
                    res = solve(pos+1, root)
                    if res > 0:
                        result += node.valid * res
                        cache[pos+1] = res
        pos += 1
    return result

morseAlphabet = {"A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.", "H": "....", "I": "..",
                 "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.",
                 "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--", "Z": "--.."}

inverseMorseAlphabet=dict((v,k) for (k,v) in morseAlphabet.items())

cache = {}
root = TreeNode()

l = input()

s = time.time()

n = int(input())
for i in range(n):
    w = input()
    w = w.upper()
    code = encode(w)
    insert(root, code)

result = solve(0, root)

print(time.time() - s, file=sys.stderr)

print(result)

