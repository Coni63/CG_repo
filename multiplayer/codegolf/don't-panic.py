i=int
*a,d,e,f,g,h=list(map(i,input().split()))
z={d:e}
for _ in "*"*h:j,k=input().split();z[i(j)]=i(k)
while 1:
    l,m,o=input().split()
    l=int(l);m=int(m);o=len(o)
    print("BLOCK" if (l!=-1) and ((m>z[l] and o>4) or (m<z[l] and o<5)) else "WAIT")