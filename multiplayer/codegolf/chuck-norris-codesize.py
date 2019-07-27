import itertools as g
b,a,*r="".join([format(ord(x),'07b')for x in input()]),"0",
for k,v in g.groupby(b):r+=[(2-int(k))*a,a*len(list(v))]
print(*r)
