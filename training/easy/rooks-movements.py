import sys
import math

cols = "abcdefgh" 
res = []

other = [[], []]

init_pos = input()
col, row = init_pos
row = int(row)
col = cols.index(col)

nb_pieces = int(input())
for i in range(nb_pieces):
    colour, pos = input().split()
    colour = int(colour)
    other[colour].append(pos)
    
for i in range(col+1, 8):
    pos_name = cols[i] + str(row)
    if pos_name in other[0]:
        break
    elif pos_name in other[1]:
        res.append("R{}x{}".format(init_pos, pos_name))
        break
    else:
        res.append("R{}-{}".format(init_pos, pos_name))
        
for i in range(col, 0, -1):
    pos_name = cols[i-1] + str(row)
    if pos_name in other[0]:
        break
    elif pos_name in other[1]:
        res.append("R{}x{}".format(init_pos, pos_name))
        break
    else:
        res.append("R{}-{}".format(init_pos, pos_name))
        
for i in range(row, 8):
    pos_name = cols[col] + str(i+1)
    if pos_name in other[0]:
        break
    elif pos_name in other[1]:
        res.append("R{}x{}".format(init_pos, pos_name))
        break
    else:
        res.append("R{}-{}".format(init_pos, pos_name))
        
for i in range(row-1, 0, -1):
    pos_name = cols[col] + str(i)
    if pos_name in other[0]:
        break
    elif pos_name in other[1]:
        res.append("R{}x{}".format(init_pos, pos_name))
        break
    else:
        res.append("R{}-{}".format(init_pos, pos_name))
        
res.sort()
for each in res:
    print(each)

