import sys
import math

def check_order(tab, index):
    result = True
    for i in range(len(tab)):
        if i <= index-1 and tab[i] == 0:
            result = False
        elif i >= index and tab[i] == 1:
            result = False
    return result

def find_swap(order):
    reverse = order[::-1]
    Flag1 = False
    Flag2 = False
    swap_done = False
    index_first_zero = -1
    index_last_one = -1
    for i in range(len(order)):
        if order[i] == 0 and index_first_zero == -1:
            index_first_zero = i
            Flag1 = True
        if reverse[i] == 1 and index_last_one == -1:
            index_last_one = n-i-1
            Flag2 = True
        if Flag1 and Flag2 and swap_done == False:   
            order[index_first_zero], order[index_last_one] = order[index_last_one], order[index_first_zero]
            swap_done = True
            print("switch" + str(index_first_zero) + " et " + str(index_last_one), file=sys.stderr)
            print(order, file=sys.stderr)
            
    return order

ordre = []
inverse = []
nb_one = 0

n = int(input())
for i in input().split():
    x = int(i)
    ordre.append(x)
    if x == 1:
        nb_one += 1

inverse = ordre[::-1]

print(ordre, file=sys.stderr)
print(sorted(ordre, reverse=True), file=sys.stderr)

nb_swap = 0

is_sorted = check_order(ordre, nb_one)

while is_sorted == False:
    ordre = find_swap(ordre)
    nb_swap+=1   
    is_sorted = check_order(ordre, nb_one)
    print(is_sorted, file=sys.stderr)
    
print(nb_swap)
        

# To debug: print("Debug messages...", file=sys.stderr)


