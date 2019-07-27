import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

x_1, y_1, r_1 = [int(i) for i in input().split()]
x_2, y_2, r_2 = [int(i) for i in input().split()]

print("Cercle 1 : centre (%s,%s) - rayon %s" % (x_1, y_1, r_1) , file=sys.stderr)
print("Cercle 1 : centre (%s,%s) - rayon %s" % (x_2, y_2, r_2) , file=sys.stderr)

d = ((x_2-x_1)**2+(y_2-y_1)**2)**0.5
print("Distance between circles : %s"% d, file=sys.stderr)

if d >= r_1+r_2:
    area = 0
elif d < abs(r_1-r_2):
    area = math.pi*min(r_1,r_2)**2
else:
    part1 = (r_1**2)*math.acos((d**2+r_1**2-r_2**2)/(2*d*r_1))
    part2 = (r_2**2)*math.acos((d**2+r_2**2-r_1**2)/(2*d*r_2))
    part3 = 0.5 * ((-d+r_1+r_2)*(d+r_1-r_2)*(d+r_2-r_1)*(d+r_1+r_2))**0.5
    area = round(part1+part2-part3 , 2)
    
print('{:.2f}'.format(area))

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)


