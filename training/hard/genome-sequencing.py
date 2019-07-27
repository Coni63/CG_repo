import sys
import math
import re

def concat(subseq, sequence):
    
    if re.search(subseq, sequence):
        #print(subseq + " is in " + sequence, file=sys.stderr)
        return sequence
    else:
        pattern = subseq
        found = False
        a = len(pattern)-1
        #print(sequence, file=sys.stderr)
        #print(pattern, file=sys.stderr)
        while a >= 1 and found == False:
            #print(pattern[:a], file=sys.stderr)
            #print(pattern[-a:], file=sys.stderr)
            prog_deb = re.compile(pattern[:a])
            prog_fin = re.compile(pattern[-a:])
            print("looking for "+pattern[-a:]+" in "+sequence[:a], file=sys.stderr)
            result_deb = prog_fin.search(sequence, 0, a)
            print("looking for "+pattern[:a]+" in "+sequence[-a:], file=sys.stderr)
            result_fin = prog_deb.search(sequence, len(sequence)-a,len(sequence))
        
            if result_deb != None:
                print("result_deb", file=sys.stderr)
                sequence = subseq + sequence[a:]
                found = True
                return sequence
            elif result_fin != None: 
                print("result_fin", file=sys.stderr)
                sequence = sequence[:-a] + subseq
                found = True
                return sequence
            else:
                print("rien", file=sys.stderr)
                a -=1
        print("+++", file=sys.stderr)
        return sequence+subseq
                

phrase = ""
arr = []

n = int(input())
for i in range(n):
    mot = input()
    arr.append(mot)

#arr = ['BACA', 'GATTACA', 'TT']
arr.sort(key=len, reverse=True)
print(arr, file=sys.stderr)

for each in arr:    
    if phrase == "":
        phrase = each
    else:
        phrase = concat(each, phrase)
        print(phrase, file=sys.stderr)


print(len(phrase))

# To debug: print("Debug messages...", file=sys.stderr)