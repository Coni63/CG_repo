import sys
import math
import numpy as np
import time
from scipy import signal

OFFSET_PARTITION = 10

w, h = [int(i) for i in input().split()]
print(w,h, file=sys.stderr)

image = input().split()

start_time = time.time() 

#generation d'un array de 0 (White) ou 1(Black) de w*h de long 
img_array = []
for index in range(int(len(image)/2)):
    if image[2*index] == "B":
        img_array += [1] * int(image[2*index+1])
    else:
        img_array += [0] * int(image[2*index+1])

#conversion en numpy matrix de w de large et h de haut avec uniquement des booleens (False = White, True = Black)
np_image = np.array(img_array, dtype=np.int8).reshape(h, w)

#suppression des parties blanches en amont et aval de la partition (10 pxl chaque coté)
np_image = np_image[:, OFFSET_PARTITION:-OFFSET_PARTITION]
h, w = np_image.shape

# find line thickness
isline = np.sum(np_image>0, axis=1) > 0.8*w
LINE_THK = isline.sum() // 5

#find space between line and index first line
idx_line = np.argwhere(isline).flatten()
FIRST_ROW = idx_line[0]
for a, b in zip(idx_line[:-1], idx_line[1:]):
    if b-a > 1:
        SPACE = b-a-1
        break

