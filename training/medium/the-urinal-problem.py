import sys
import math

n = int(input())
b = input()

best_result = None

for index in range(n):
    #print(index, b[index], file=sys.stderr)
    if b[index]!= "!":
        left_arr = b[:index]
        right_arr = b[index+1:]
        left_arr_rev = left_arr[::-1]
        print("%s-%s"%(left_arr, right_arr), file=sys.stderr)
        
        left_dist = float('inf')
        if len(left_arr_rev) > 0:
            if "!" in left_arr_rev:
                left_dist = left_arr_rev.index("!")
                
        right_dist = float('inf')
        if len(right_arr)> 0:
            if "!" in right_arr:
                right_dist = right_arr.index("!")
                
        closest_toilet = min(left_dist, right_dist)
        
        if best_result is None or closest_toilet > best_result[1]:
            best_result = (index, closest_toilet)
        
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print(best_result[0])
