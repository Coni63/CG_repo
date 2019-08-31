import sys
import math

class Position:
    def __init__(self, x):
        self.sexagesimal = x
        self.decimal = self.to_decimal()
        # print("{} -> {}".format(self.sexagesimal, math.degrees(self.decimal), file=sys.stderr))
        
    def to_decimal(self):
        letter = self.sexagesimal[0]
        if letter in "NS":
            degree = int(self.sexagesimal[1:3])
            minute = int(self.sexagesimal[3:5])
            seconde = int(self.sexagesimal[5:])
        else:
            degree = int(self.sexagesimal[1:4])
            minute = int(self.sexagesimal[4:6])
            seconde = int(self.sexagesimal[6:])
        angle = degree + minute/60 + seconde/3600
        # print(degree, minute, seconde, file=sys.stderr)
        if letter in "EN":
            return math.radians(angle)
        else:
            return -math.radians(angle)
    
    def __repr__(self):
        return "{:.3f}".format(self.decimal)
            
class City:
    def __init__(self, name, latitude, longitude):
        self.name = name
        self.latitude = Position(latitude)
        self.longitude = Position(longitude)
        self.message = ""
        
    def distance_to(self, other_lat, other_long):
        x = math.sin((self.latitude.decimal-other_lat.decimal)/2)**2
        y = math.cos(self.latitude.decimal) * math.cos(other_lat.decimal) * math.sin((self.longitude.decimal-other_long.decimal)/2)**2
        d = 2*6371*math.asin(math.sqrt(x + y))
        return round(d)
        
    def __repr__(self):
        return "{} ({}, {})".format(self.name, self.latitude, self.longitude)

# print(Position("N510734").decimal,  file=sys.stderr)

cities = []
n = int(input())  # number of capitals
m = int(input())  # number of geolocations for which to find the closest capital
for i in range(n):
    cities.append(City(*input().split()))

print("", file=sys.stderr)

for i in range(n):
    cities[i].message = input()
    print(cities[i], file=sys.stderr)
    
print("", file=sys.stderr)
    
for i in range(m):
    travel_lat, tarvel_lon = input().split()
    travel_lat = Position(travel_lat)
    tarvel_lon = Position(tarvel_lon)
    dmin = 1e10
    closest_city = None
    for city in cities:
        d = city.distance_to(travel_lat, tarvel_lon)
        print(city.name, d, file=sys.stderr)
        if d < dmin:
            dmin = d
            closest_city = [city]
        elif d == dmin:
            closest_city += [city]
    print("", file=sys.stderr)
    print(*[x.message for x in closest_city])
    print("", file=sys.stderr)
