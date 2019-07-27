import sys
import math
import operator

table = [0]*30
freq = {}
alphabet = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
position = 0

magic_phrase = input()
print(magic_phrase , file=sys.stderr)

for each in alphabet:
    freq[each] = magic_phrase.count(each)
print(freq , file=sys.stderr)

sorted_freq = sorted(freq.items(), key=operator.itemgetter(1), reverse=True)
print(sorted_freq , file=sys.stderr)

assigned_position = {}
current_free_index = 1
for letter, frequence in sorted_freq:
    if frequence > 2:
        assigned_position[letter] = current_free_index
        current_free_index += 1

print(assigned_position , file=sys.stderr)

sentence = ""
#for letters in magic_phrase:
i=0
while i < len(magic_phrase):
    letters = magic_phrase[i]
    index_required = alphabet.index(letters)
    current_index = table[position]
    
    #print("voulu / %s -> current : %s " % (letters, alphabet[current_index]),file=sys.stderr)
    #print(index_required, current_index,file=sys.stderr)
    """
    if letters in assigned_position.keys():
        if position < assigned_position[letters]:
            sentence += ">"
            position += 1
        elif position > assigned_position[letters]:
            sentence += "<"
            position -= 1
        else:
            if current_index == index_required:
                sentence += "."
                i += 1
            else:
                if index_required > current_index:
                    #print("sens direct",file=sys.stderr)
                    sens_pos = index_required-current_index
                    sens_neg = 27 - sens_pos
                else:
                    #print("sens indirect",file=sys.stderr)
                    sens_neg = -(index_required-current_index)
                    sens_pos = 27 - sens_neg
                    
                #print("sens + : %s / sens - : %s"%(sens_pos, sens_neg), file=sys.stderr)
                
                if sens_pos <= sens_neg:
                    sentence += "+"
                    table[position] += 1
                    table[position] = table[position]%27
                else:
                    sentence += "-"
                    table[position] -= 1
                    if table[position] < 0:
                        table[position] = 26
    else:
    """
    if current_index == index_required:
        sentence += "."
        i += 1
    else:
        if index_required > current_index:
            #print("sens direct",file=sys.stderr)
            sens_pos = index_required-current_index
            sens_neg = 27 - sens_pos
        else:
            #print("sens indirect",file=sys.stderr)
            sens_neg = -(index_required-current_index)
            sens_pos = 27 - sens_neg
            
        #print("sens + : %s / sens - : %s"%(sens_pos, sens_neg), file=sys.stderr)
        
        if sens_pos <= sens_neg:
            sentence += "+"
            table[position] += 1
            table[position] = table[position]%27
        else:
            sentence += "-"
            table[position] -= 1
            if table[position] < 0:
                table[position] = 26

print(sentence)           
#print("+.>-.")
