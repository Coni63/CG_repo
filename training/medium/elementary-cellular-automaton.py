import sys
import math

def convert(mot):
    new_mot = ""
    for i in range(1, len(mot)-1):
        pattern = mot[i-1:i+2]
        #print(pattern, file = sys.stderr)
        new_mot += table[pattern]
    
    wrapper_new_mot = new_mot[-1] + new_mot + new_mot[0]
    return wrapper_new_mot 

r = int(input())
n = int(input())
start_pattern = input()

word = start_pattern.replace('.','0').replace('@', '1')
print("Converting \"%s\" %s times with key %s" % (word, n, r), file = sys.stderr)

r_binary = "{0:#b}".format(r)[2:].zfill(8)
#print(r_binary, file=sys.stderr)

table = {"000":"0", "001":"0", "010":"0", "011":"0", "100":"0", "101":"0", "110":"0", "111":"0"}

if r_binary[0] == "1" : table["111"]="1"
if r_binary[1] == "1" : table["110"]="1"
if r_binary[2] == "1" : table["101"]="1"
if r_binary[3] == "1" : table["100"]="1"
if r_binary[4] == "1" : table["011"]="1"
if r_binary[5] == "1" : table["010"]="1"
if r_binary[6] == "1" : table["001"]="1"
if r_binary[7] == "1" : table["000"]="1"
#print(table, file=sys.stderr)

wrapped_word = word[-1] + word + word[0]
print("wrapped_word = %s" %wrapped_word, file=sys.stderr)

print(start_pattern)

for _ in range(n-1):
    wrapped_word = convert(wrapped_word)
    print_word = wrapped_word.replace('0','.').replace('1','@')
    print(print_word[1:-1])
