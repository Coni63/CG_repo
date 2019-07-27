import sys
import math

solution = 0
queue = [(0, 0)]
board = []
m = int(input())
n = int(input())
for i in range(m):
    board.append([int(x) for x in input()])

while len(queue) > 0:
    row, col = queue.pop(0)

    if row == m-1 and col == n-1:
        solution +=1
        continue
    
    if row < m-1 and board[row+1][col] == 0:
        queue.append((row+1, col))
    if col < n-1 and board[row][col+1] == 0:
        queue.append((row, col+1))
        
print(solution)
