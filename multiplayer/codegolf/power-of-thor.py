a,b,x,y=map(int,input().split())
while 1:
  d=""
  if b>y:d="S";y+=1
  if b<y:d="N";y-=1
  if a>x:d+="E";x+=1
  if a<x:d+="W";x-=1
  print(d)