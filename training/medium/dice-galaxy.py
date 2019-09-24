def get(x, y):
    global mp, w, h
    if x<0 or y<0 or x>w-1 or y>h-1:return "."
    return mp[y][x]

def put(x, y, c):
    global mp
    mp[y] = mp[y][:x] + c + mp[y][x+1:]
    
def setOppo(sx, sy, c):
    global mp
    sp=[(sx, sy, 0, 0)]
    ck=[(sx, sy)]
    while sp!=[]:
        for dx, dy in zip([-1,1,0,0], [0,0,-1,1]):
            x, y, fx, fy = sp[0]
            nx = x + dx
            ny = y + dy
            if (nx, ny) in ck or get(nx, ny)==".":continue
            ck+=[(nx, ny)]
            if fx == fy == 0:
                fx = dx
                fy = dy
            if fx!=0 and nx - sx == fx * 2:
                put(nx, ny, c)
                return mp
            if fy!=0 and ny - sy == fy * 2:
                put(nx, ny, c)
                return mp  
            sp+=[(nx, ny, fx, fy)]
        del sp[0]
    return mp

w = int(input())
h = int(input())
mp = []
for _ in range(h):mp += [input().replace("6", "#")]
for y in range(h):
    for x in range(w):
        if get(x,y) == "1":
            mp = setOppo(x, y, "6")
for i in mp:print(i)
