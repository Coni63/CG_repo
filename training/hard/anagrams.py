import sys
import math

def split_by_n(word, l):
    while word:
        size = l.pop(0)
        yield word[:size]
        word = word[size:]

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#   Phase 4
print("### Phase 4 ###", file=sys.stderr)

phrase = input()
#print(phrase, file=sys.stderr)

size_reversed = [len(x) for x in phrase.split()][::-1]
#print(size_reversed, file=sys.stderr)

phrase_merge = ''.join(phrase.split())
#print(phrase_merge, file=sys.stderr)

#   Phase 3
#print("### Phase 3 ###", file=sys.stderr)

letter = ""
position_array = []
for i in range(len(phrase_merge)):
    if (alphabet.index(phrase_merge[i])+1) % 4 == 0:
        letter += phrase_merge[i]
        position_array.append(i)

#print(letter, position_array, file=sys.stderr)

if len(position_array) > 0:
    letters_shifted = letter[-1] + letter[:-1]
#    print(letters_shifted, file=sys.stderr)

print(phrase_merge, file=sys.stderr)
for j in range(len(position_array)):
    phrase_merge = phrase_merge[:position_array[j]] + letters_shifted[j] + phrase_merge[position_array[j]+1:]
#print(phrase_merge, file=sys.stderr)

#   Phase 2
print("### Phase 2 ###", file=sys.stderr)

letter = ""
position_array = []
for k in range(len(phrase_merge)):
    if (alphabet.index(phrase_merge[k])+1) % 3 == 0:
        letter += phrase_merge[k]
        position_array.append(k)

#print(letter, position_array, file=sys.stderr)

letters_shifted = letter[1:] + letter[0]
#print(letters_shifted, file=sys.stderr)

#print(phrase_merge, file=sys.stderr)
for l in range(len(position_array)):
    phrase_merge = phrase_merge[:position_array[l]] + letters_shifted[l] + phrase_merge[position_array[l]+1:]
#print(phrase_merge, file=sys.stderr)

#   Phase 1
#print("### Phase 1 ###", file=sys.stderr)

letter = ""
position_array = []
for m in range(len(phrase_merge)):
    if (alphabet.index(phrase_merge[m])) % 2 == 1:
        letter += phrase_merge[m]
        position_array.append(m)
        
#print(letter, position_array, file=sys.stderr)

letters_reversed = letter[::-1]
#print(letters_reversed, file=sys.stderr)

#print(phrase_merge, file=sys.stderr)
for n in range(len(position_array)):
    phrase_merge = phrase_merge[:position_array[n]] + letters_reversed[n] + phrase_merge[position_array[n]+1:]
#print(phrase_merge, file=sys.stderr)

# Splitting

phrase_stage_4 = " ".join(list(split_by_n(phrase_merge, size_reversed)))
print(phrase_stage_4)

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

