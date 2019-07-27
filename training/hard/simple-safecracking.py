import sys
import math
import re

def shift(arr):
    new_message = []
    for number in arr:
        new_number = ""
        for digit in number:
            digit = str(digit)
            if digit == 'z':
                new_index = ord('a')
            else:    
                new_index = ord(digit)+1  
            new_number += chr(new_index)
        new_message.append(new_number)
    return new_message

number = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

msg = input().split()[-1].split('-')

for _ in range(0, 26):
    msg = shift(msg)
    if msg[0] in number.keys():
        result = ""
        for each in msg:
            result += number[each]

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print(result)
