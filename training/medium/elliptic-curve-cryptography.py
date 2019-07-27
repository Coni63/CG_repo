import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def extended_gcd(aa, bb):
    lastremainder, remainder = abs(aa), abs(bb)
    x, lastx, y, lasty = 0, 1, 1, 0
    while remainder:
        lastremainder, (quotient, remainder) = remainder, divmod(lastremainder, remainder)
        x, lastx = lastx - quotient*x, x
        y, lasty = lasty - quotient*y, y
    return lastremainder, lastx * (-1 if aa < 0 else 1), lasty * (-1 if bb < 0 else 1)

def mod_inverse(a, m):
	g, x, y = extended_gcd(a, m)
	return x % m

class EllipticCurve(object):
    def __init__(self, a, b, p):
        self.a = a
        self.b = b
        self.p = p

    def __eq__(self, C):
        return (self.a, self.b) == (C.a, C.b)

    def has_point(self, x, y):
        return (y ** 2) % self.p == (x ** 3 + self.a * x + self.b) % self.p


class Point(object):
    """A point on a specific curve."""
    def __init__(self, curve, point):
        self.curve = curve
        self.x = point[0] % curve.p
        self.y = point[1] % curve.p

    def __getitem__(self, index):
        return [self.x, self.y][index]

    def __eq__(self, Q):
        return (self.curve, self.x, self.y) == (Q.curve, Q.x, Q.y)

    def __neg__(self):
        return Point(self.curve, self.x, -self.y)
    
    def __add__(self, Q):
        xp, yp, xq, yq = self.x, self.y, Q.x, Q.y
        m = None

        # P == Q
        if self == Q:
            if self.y == 0:
                R = Inf(self.curve)
            else:
                m = ((3 * xp * xp + self.curve.a) * mod_inverse(2 * yp, self.curve.p)) % self.curve.p
        # Common case
        else:
            m = ((yq - yp) * mod_inverse(xq - xp, self.curve.p)) % self.curve.p

        if m is not None:
            xr = (m ** 2 - xp - xq) % self.curve.p
            yr = (m * (xp - xr) - yp) % self.curve.p
            R = Point(self.curve, (xr, yr))

        return R
    
    def __mul__(self, n):
        n = n % self.curve.p
        Q = self
        R = Inf(self.curve)

        i = 1
        while i <= n:
            if n & i == i:
                R = R + Q
            Q = Q + Q
            i = i << 1
        return R

    def __rmul__(self, n):
        return self * n


class Inf(Point):
    """The custom infinity point."""
    def __init__(self, curve):
        self.curve = curve

    def __eq__(self, Q):
        return isinstance(Q, Inf)

    def __neg__(self):
        """-0 = 0"""
        return self
    
    def __add__(self, Q):
        """P + 0 = P"""
        return Q


P = 0x3fddbf07bb3bc551
A = 0
B = 7
GX = 0x69d463ce83b758e
GY = 0x287a120903f7ef5c
G = (GX, GY)

print((GY**2)%P == (GX**3 + B)%P, file=sys.stderr)

curve = EllipticCurve(A, B, P)
point = Point(curve, G)

n = int(input())
for i in range(n):
    k = int(input(), 16)
    target = k * point
    print(hex(target[0]))
