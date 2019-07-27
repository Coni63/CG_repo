import sys
import math

def split_by_n( seq, n ):
    """A generator to divide a sequence into chunks of n units."""
    while seq:
        yield seq[:n]
        seq = seq[n:]


def get_index(letter):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if alphabet.find(letter)!=-1:
        return alphabet.index(letter)
    else:   
        return 26
    
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

l = int(input())
h = int(input())
mot = input().upper()

for _ in range(h):
    row = input()
    matrix=list(split_by_n(row,l))
    print("".join([matrix[get_index(letter)] for letter in mot]))