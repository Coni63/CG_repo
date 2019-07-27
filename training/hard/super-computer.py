import sys
import math

def slot_suivant(fin_comp):
    if fin_comp < start_arr[-1]:
        for each in start_arr:
            if each > fin_comp:
                return each
    else:
        return -1

def expand(ce_node):
    if ce_node in memo:
        return memo[ce_node]
    else:
        calcul = 0
        for end_of_run in arr[ce_node]:
            next_start = slot_suivant(end_of_run)
            if next_start != -1:
                a = expand(next_start)+1
                calcul = max(calcul, a)
        memo[ce_node] = calcul
        return calcul
        
memo = {}
arr = {}
start_arr = []

n = int(input())
for i in range(n):
    j, d = [int(j) for j in input().split()]
    if j in arr.keys():
        arr[j].append(j+d-1)
    else:
        arr[j] = [j+d-1]
    if j not in start_arr:
        start_arr.append(j)

#start_arr = list(arr.keys())
start_arr.sort()

print(start_arr, file=sys.stderr)
calcul = expand(start_arr[0])
print(calcul+1)

#print(list_node, file=sys.stderr)


