a,b,x,y=map(int,input().split())
while 1:
 d=["","S"][b>y];y+=b>y
 if a>x:d+="E";x+=1
 if a<x:d+="W";x-=1
 print(d)