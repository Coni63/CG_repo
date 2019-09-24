import sys
import math
import re
import numpy as np

class Quatenion:
    def __init__(self, i, j, k, l):
        self.i=i  # a2
        self.j=j  # a3
        self.k=k  # a4
        self.l=l  # a1
        
    def __repr__(self):
        # return f"{self.i}i {self.j}j {self.k}k {self.l}"
        return f"{self.i}, {self.j}, {self.k}, {self.l}"
        
    def __str__(self):
        r = ""
        if self.i == 0:
            pass
        elif self.i == 1:
            r += "i"
        elif self.i == -1:
            r += "-i"
        else:
            r += f"{self.i}i"
            
        if self.j == 0:
            pass
        elif self.j == 1:
            r += "+j"
        elif self.j == -1:
            r += "-j"
        else:
            r += "{:+d}j".format(self.j)
            
        if self.k == 0:
            pass
        elif self.k == 1:
            r += "+k"
        elif self.k == -1:
            r += "-k"
        else:
            r += "{:+d}k".format(self.k)
            
        if self.l == 0:
            pass
        elif self.l == 1:
            r += "+1"
        elif self.l == -1:
            r += "-1"
        else:
            r += "{:+d}".format(self.l)
        
        return r
            
    def asMatrix(self):
        #http://culturemath.ens.fr/maths/pdf/logique/quaternions.pdf
        a, b, c, d = self.l, self.i, self.j, self.k
        return np.array([
            [a, -b, -c, -d], 
            [b,  a, -d,  c], 
            [c,  d,  a, -b], 
            [d, -c,  b,  a]])
        
    def __mul__(self, other):
        # http://mathworld.wolfram.com/Quaternion.html
        # a1, a2, a3, a4 = self.l, self.i, self.j, self.k
        # b1, b2, b3, b4 = other.l, other.i, other.j, other.k
        # new_i = a1*b2 + a2*b1 + a3*b4 - a4*b3
        # new_j = a1*b3 - a2*b4 + a3*b1 + a4*b2
        # new_k = a1*b4 + a2*b3 - a3*b2 + a4*b1
        # new_l = a1*b1 - a2*b2 - a3*b3 - a4-b4
        # return Quatenion(new_i, new_j, new_k, new_l)
        r = self.asMatrix().dot(other.asMatrix())
        r = r[:, 0].flatten()
        return Quatenion(r[1], r[2], r[3], r[0])

Qs = []
expr = input()
# expr = "(2i+2j)(j+1)"
print(expr, file=sys.stderr)

for g in re.findall(r"\(([^)]+)", expr):
    # print(g, file=sys.stderr)
    
    i_expr = re.findall(r"([-]?\d*)i", g)
    if len(i_expr) > 0:
        if i_expr[0] == "":
            i_expr = 1
        elif i_expr[0] == "-":
            i_expr = -1
        else:
            i_expr = int(i_expr[0])
    else:
        i_expr = 0
    # print(i_expr, file=sys.stderr)
    
    j_expr = re.findall(r"([-]?\d*)j", g)
    if len(j_expr) > 0:
        if j_expr[0] == "":
            j_expr = 1
        elif j_expr[0] == "-":
            j_expr = -1
        else:
            j_expr = int(j_expr[0])
    else:
        j_expr = 0
    # print(j_expr, file=sys.stderr)
    
    k_expr = re.findall(r"([-]?\d*)k", g)
    if len(k_expr) > 0:
        if k_expr[0] == "":
            k_expr = 1
        elif k_expr[0] == "-":
            k_expr = -1
        else:
            k_expr = int(k_expr[0])
    else:
        k_expr = 0
    # print(k_expr, file=sys.stderr)
    
    l_expr = re.findall(r"[-]?\d+$", g)
    if len(l_expr) > 0:
        if l_expr[0] == "":
            l_expr = 1
        elif l_expr[0] == "-":
            l_expr = -1
        else:
            l_expr = int(l_expr[0])
    else:
        l_expr = 0
    # print(l_expr, file=sys.stderr)
    
    q = Quatenion(i_expr, j_expr, k_expr, l_expr)
    # print(repr(q), file=sys.stderr)
    Qs.append(q)

r = Qs[0]
for i in range(1, len(Qs)):
    r *= Qs[i]

# print(repr(r), file=sys.stderr)

print(str(r))
