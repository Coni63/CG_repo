import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def to_rad(deg):
    v = deg.replace(",",".")
    v = float(v)
    return v*(2*math.pi)/360
    
def get_dist(a,b,c,d):
    x = (a-c)*math.cos((a+c)/2)
    y = d-b
    d = math.sqrt(math.pow(x,2)+math.pow(y,2))
    return d

lon = input()
lat = input()
n = int(input())

lon = to_rad(lon)
lat = to_rad(lat)

listing = []
dist_min = 1500
nom = ""

for i in range(n):
    defib = input()
    listing=defib.split(";")
        
    distance = get_dist(lon, lat, to_rad(listing[4]), to_rad(listing[5]))
    
    if distance < dist_min:
       dist_min = distance
       nom = listing[1]

print(nom)  



# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)


