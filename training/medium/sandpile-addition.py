import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

class Matrix:
    def __init__(self, size):
        self.size = size
        self.matrix = []
        
    def sum_matrix(self, M):
        R = Matrix(self.size)
        for i in range(self.size):
            l = []
            for j in range(self.size):
                l.append(self.matrix[i][j] + M.matrix[i][j])
            R.matrix.append(l)
        return R
        

    def add_line(self, line):
        self.matrix.append([int(x) for x in line])
        
    def show(self):
        for each in self.matrix:
            print(each, file=sys.stderr)
    
    def sandpile(self):
        continuer = True
        while continuer:
            continuer = False
            for i in range(self.size):
                l = []
                for j in range(self.size):
                    if self.matrix[i][j] >= 4:
                        self.matrix[i][j] -= 4
                        continuer = True
                        if i > 0:
                            self.matrix[i-1][j] += 1
                        if i < self.size -1:
                            self.matrix[i+1][j] += 1
                        if j > 0:
                            self.matrix[i][j-1] += 1
                        if j < self.size -1:
                            self.matrix[i][j+1] += 1
    
    def print_result(self):
        for line in self.matrix:
            print(''.join([str(x) for x in line]))


n = int(input())
M1 = Matrix(n) 
M2 = Matrix(n) 

for i in range(n):
    row = input()
    M1.add_line(row)
    
for i in range(n):
    row = input()
    M2.add_line(row)
    
M1.show()
M2.show()

R = M1.sum_matrix(M2)
R.show()

R.sandpile()
R.show()

R.print_result()

    
