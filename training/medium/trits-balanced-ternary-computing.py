import sys
import math

class Ternary:
    def __init__(self, s=None, n=None):
        if s is not None:
            self.s = s
            self.n = self.to_int()
        elif n is not None:
            self.n = n
            self.s = self.to_str()

    def to_int(self):
        n = 0
        maping = {"1":1, "T":-1, "0":0}
        for i, v in enumerate(self.s[::-1]):
            n += maping[v] * 3**i
        return n
        
    def to_str(self):
        s=""
        n = self.n
        while True:
            r = (n + 30000)%3
            r = int(r)
            n -= [0, 1, -1][r]
            n /= 3
            s = "01T"[r] + s
            if n == 0: 
                return s
        
    def __add__(self, other):
        total = self.n + other.n
        return Ternary(n=total)
        
    def __sub__(self, other):
        total = self.n - other.n
        return Ternary(n=total)
        
    def __mul__(self, other):
        total = self.n * other.n
        return Ternary(n=total)
        
    def __lshift__(self, other):  
        total = self.n * (3**other.n)
        return Ternary(n=total)
        
    def __rshift__(self, other):
        total = self.n // (3**other.n)
        return Ternary(n=total)
        
    def __repr__(self):
        return "{}={}".format(self.s, self.n)

lhs = Ternary(s=input())
op = input()
rhs = Ternary(s=input())

print(lhs, file=sys.stderr)
print(rhs, file=sys.stderr)

if op == "+":
    res = lhs + rhs
if op == "-":
    res = lhs - rhs
if op == "*":
    res = lhs * rhs
if op == ">>":
    res = lhs >> rhs
if op == "<<":
    res = lhs << rhs

print(res, file=sys.stderr)
    
print(res.s)
