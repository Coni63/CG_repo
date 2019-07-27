import sys

while True:
    mountain_h = [int(input()) for _ in range(8)]  # represents the height of one mountain, from 9 to 0.
    print(mountain_h.index(max(mountain_h)))
    
    # Write an action using print
    # To debug: 

    # The number of the mountain to fire on.
    
