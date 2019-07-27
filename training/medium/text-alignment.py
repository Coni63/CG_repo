import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

data = {}
max_size = 0

alignment = input()
print("Alignment: %s" %alignment, file=sys.stderr)


n = int(input())
for i in range(n):
    text = input().strip()
    nb_of_words = len(text.split())
    nb_of_spaces = nb_of_words-1
    nb_of_chars = len(text)
    if nb_of_chars > max_size:
        max_size = nb_of_chars 
    data[i]={"text": text, "nb_of_words": nb_of_words, "nb_of_spaces": nb_of_spaces, "nb_of_chars": nb_of_chars}
    print("%s words - %s spaces - %s chars" % (nb_of_words, nb_of_spaces, nb_of_chars), file=sys.stderr)
    
    
for i in range(n):
    if alignment == "LEFT":
        res = data[i]["text"]
    elif alignment == "RIGHT":
        spaces_to_share = max_size - data[i]["nb_of_chars"]
        res = " "* spaces_to_share + data[i]["text"]
    elif alignment == "CENTER":
        spaces_to_share = max_size - data[i]["nb_of_chars"]
        spaces_to_shift = int(spaces_to_share/2)
        res = " "* spaces_to_shift + data[i]["text"]   
    elif alignment == "JUSTIFY":
        spaces_to_share = max_size - data[i]["nb_of_chars"]
        spaces_width = spaces_to_share / data[i]["nb_of_spaces"]
        #total_width = [spaces_width*i for i in range(data[i]["nb_of_spaces"])]
        #print(total_width, file=sys.stderr)
        sentence = data[i]["text"].split()
        res = (" "*(1 + int(spaces_width))).join(sentence)
    
    print(res)
    
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

