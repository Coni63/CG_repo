import sys
import math

def ColToExcel(col): # col is 1 based
    excelCol = str()
    div = col 
    while div:
        (div, mod) = divmod(div-1, 26) # will return (x, 0 .. 25)
        excelCol = chr(mod + 65) + excelCol

    return excelCol
    
def ExceltoCol(mot):
    mot = mot[::-1]
    index = 0
    val = 0
    for letter in mot:
        num = ord(letter)-64
        val += num*(26**index)
        index += 1
    return str(val)
    
n = int(input())
arr = [x for x in input().split()]
res = []

for each in arr:
    if each.isdigit():
        res.append(ColToExcel(int(each)))
    else:
        res.append(ExceltoCol(each))
        
print(" ".join(res))  

# To debug: print(mess, file=sys.stderr)
