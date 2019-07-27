size = lambda I: (len(I[0]),len(I))
range_clamp = lambda A,a,b,B: range(max(a,A),min(b,B))

def energy(I, x, y):
    return   (abs(I[y][x+1]-I[y][x-1]) if 0<x<len(I[0])-1 else 0)  \
           + (abs(I[y+1][x]-I[y-1][x]) if 0<y<len(I)-1    else 0)

def carve(I):
    W,H = size(I)
    E = [[energy(I,x,y) for x in range(W)] for y in range(H)]
    for y in range(H-2,-1,-1):
        for x in range(W):
            E[y][x] += min(E[y+1][x0] for x0 in range_clamp(0,x-1,x+2,W))
    x = min(range(W), key=(lambda x: E[0][x]))
    print(E[0][x])  # PROBLEM OUTPUT
    Path = [x]*H
    for y in range(1,H):
        Path[y] = min(range_clamp(0,Path[y-1]-1,Path[y-1]+2,W), key=(lambda x0: E[y][x0]))
    J = [I[y][:Path[y]]+I[y][Path[y]+1:] for y in range(H)]
    return J

def pgm(I):
    W,H = size(I)
    O = ['P2', '%d %d'%(W,H), '255']
    for y in range(H):
        O.append(' '.join(map(str,I[y])))
    return '\n'.join(O)

input()
W,H = map(int,input().split())
V = int(input().split()[1])
input()
I = [list(map(int,input().split())) for _ in range(H)]
for _ in range(W-V):
    I = carve(I)

