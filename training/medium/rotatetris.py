import itertools

background = []
piece     = []
rotations  = [[],[],[],[]]
square_is_full = False

h = int(input())
w = int(input())
for irow in range(h):
    row=input()
    for icol in range(len(row)):
        ch = row[icol]
        if ch == '.':
            coor = [icol,irow]
            background.append(coor)

h2 = int(input())
w2 = int(input())
for irow in range(h2):
    row=input()
    piece.append([])
    for icol in range(len(row)):
        ch = row[icol]
        coor = [icol,irow]
        piece[irow].append(ch)

for idirection in range(4):
    piece = list(itertools.zip_longest(*piece[::-1]))[::-1][::-1]

    for irow in range(len(piece)):
        row = piece[irow]
        for icol in range(len(row)):
            ch = row[icol]
            if ch == '#':
                coor = [icol,irow]
                rotations[idirection].append(coor)

first_coor_in_background_x, first_coor_in_background_y = 0, 0
idirection=0
while not square_is_full and idirection<4:
    rotation = rotations[idirection]
    try:
        first_coor_in_background_x = background[0][0]-rotation[0][0]
        first_coor_in_background_y = background[0][1]-rotation[0][1]
    except:
        first_coor_in_background_x = 0
        first_coor_in_background_y = 0
        
    for icoor in range(len(rotation)):
        x,y = rotation[icoor]
        x += first_coor_in_background_x
        y += first_coor_in_background_y
        rotations[idirection][icoor] = [x,y]

    if rotation==background:
        square_is_full=True
        break
    idirection+=1
"""
print()
print('+---------------------------HELP--------------------------')
print('| background:', background )
print('| piece:     ', piece      )
print('| rotations: ', rotations  )
print('| square_is_full:', square_is_full )
print('| first_coor_in_background_x:', first_coor_in_background_x )
print('| first_coor_in_background_y:', first_coor_in_background_y )
print('+---------------------------------------------------------')
print()
"""
if square_is_full:
    print('FULL')
else:
    print('HOLE')

