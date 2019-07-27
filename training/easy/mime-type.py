import sys
import math

n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.

table = {} 

for i in range(n):
    # ext: file extension
    # mt: MIME type.
    ext, mt = input().split(" ")  
    table[ext.lower()] = mt 
    
for i in range(q):
    fname = input()  # One file name per line.
    if fname.find(".")!=-1:
        splitted = fname.split(".")[-1].lower()
        if splitted in table:
            print(table[splitted])
        else:
            print("UNKNOWN")
    else:
        print("UNKNOWN")

        
# To debug: print("Debug messages...", file=sys.stderr)

