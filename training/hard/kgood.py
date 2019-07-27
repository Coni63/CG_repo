import sys
import math
from itertools import groupby

def custom_group(arr, maxi):
    result = 0
    for i in range(len(arr)-maxi+1):
        index = i
        dico = {}
        limit = False
        while True:
            if arr[index][0] in dico.keys():
                dico[arr[index][0]] += arr[index][1]
            elif not limit:
                dico[arr[index][0]] = arr[index][1]
            else:
                break
            index += 1
            if index == len(arr):
                break
            if len(list(dico.keys())) == maxi:
                limit = True
            
        print(dico, file = sys.stderr)    
        size = sum(list(dico.values()))
        result = max(result, size)
    return result
            

string = input()
length = int(input())

group = []
for k, g in groupby(string):
    group.append((k, len(list(g))))

print(group, file = sys.stderr)

if len(group) <= length:
    print(len(string))
else:
    print(custom_group(group, length))
