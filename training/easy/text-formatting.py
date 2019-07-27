import sys
import math
import re

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

intext = input().lower()
print(intext, file=sys.stderr)

intext = re.sub(r'\s*([.,;])\s*', r"\1", intext)
print(intext, file=sys.stderr)

intext = re.sub(r'([^A-Za-z0-9])\1+', r'\1', intext)
print(intext, file=sys.stderr)

intext = re.sub(r'([,.;])\1+', r'\1 ', intext)
print(intext, file=sys.stderr)

intext = re.sub(r'(?<=[.,;])(?=[^\s])', r' ', intext)
print(intext, file=sys.stderr)

intext = ". ".join([x.strip().capitalize() for x in intext.split(".")]).strip()

if intext[-1] != ".":
    intext += "."
    
print(intext)
