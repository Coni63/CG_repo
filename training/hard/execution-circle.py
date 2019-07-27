# https://www.youtube.com/watch?v=uCsD3ZGzMgE

n, s = [int(i) for i in input().split()]
d = input()

shift = int(bin(n)[3:] + "1", 2)

if d == "LEFT":
    print((s+shift-1)%n)
else:
    print((s-shift+n+1)%n)
