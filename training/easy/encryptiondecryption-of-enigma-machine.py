import sys
import math
import string

rotor_0 = string.ascii_uppercase 

operation = input()
pseudo_random_number = int(input())
rotors = [input() for i in range(3)]
message = input()
code = ""

if operation == "ENCODE":
    for i, letter in enumerate(message):
        shift = pseudo_random_number + i
        index = rotor_0.index(letter)
        letter = rotors[0][(index + shift)% len(rotor_0) ]
        index = rotor_0.index(letter)
        letter = rotors[1][index]
        index = rotor_0.index(letter)
        letter = rotors[2][index]
        code += letter
else:
    for i, letter in enumerate(message):
        shift = pseudo_random_number + i
        index = rotors[2].index(letter)
        letter = rotor_0[index]
        index = rotors[1].index(letter)
        letter = rotor_0[index]
        index = rotors[0].index(letter)
        letter = rotor_0[(index - shift + len(rotor_0)) % len(rotor_0)]
        code += letter
print(code)
