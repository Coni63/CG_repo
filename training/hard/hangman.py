import sys
import math
import re

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
line1 = ['+--+', '+--+', '+--+', '+--+', '+--+', '+--+', '+--+']
line2 = ['|', '|  o', '|  o', '|  o', '|  o', '|  o', '|  o']
line3 = ['|', '|', '|  |', '| /|', '| /|\\', '| /|\\', '| /|\\']
line4 = ['|\\', '|\\', '|\\', '|\\', '|\\', '|\\/', '|\\/ \\']

word = input()
chars = input().split()
print(word,file=sys.stderr)

blank = re.sub('[A-Za-z0-9]', '_', word)
print(blank,file=sys.stderr)

number_of_mistakes = 0
tried = []

for letter in chars:
    if letter in word and not letter in tried:
        tried.append(letter)
        for i in range(len(word)):
            if word[i].upper() == letter.upper():
                blank = blank[:i] + word[i] + blank[i+1:]
    else:
        number_of_mistakes += 1

number_of_mistakes = min(number_of_mistakes, 6)

print(number_of_mistakes,file=sys.stderr)
print(blank,file=sys.stderr)
print(line1[number_of_mistakes])
print(line2[number_of_mistakes])
print(line3[number_of_mistakes])
print(line4[number_of_mistakes])

print(blank)