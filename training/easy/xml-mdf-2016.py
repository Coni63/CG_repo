import sys
import math
from xml.etree import ElementTree as ET
import re
from collections import defaultdict

def BFS(tree, depth):
    counter = defaultdict(float)
    queue = [(tree, depth)]
    while len(queue) > 0:
        tree_, depth_ = queue.pop(0)
        counter[tree_.tag] += 1/depth_
        for child in tree_:
            queue.append((child, depth_+1))
    return counter


sequence = input()

xml_text = ""
for each in re.findall(r'-?\w{1}', sequence):
    if each[0] == "-":
        xml_text += "</{}>".format(each[1])
    else:
        xml_text += "<{}>".format(each[0])
        
xml_text="<fake>" + xml_text + "</fake>"  # https://stackoverflow.com/questions/38853644/python-xml-parseerror-junk-after-document-element

tree = ET.fromstring(xml_text)

counter = BFS(tree, 1)

maxi = 0
for letter, vals in counter.items():
    if vals > maxi and letter != "fake":
        maxi = vals
        balise = letter

print(balise)
