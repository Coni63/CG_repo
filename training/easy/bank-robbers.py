r = int(input())
v = int(input())

time_per_vault = []
next_step = [0 for _ in range(r)]
current_t = 0

for i in range(v):
    c, n = [int(j) for j in input().split()]
    time_per_vault.append(10**n * 5**(c-n))
    
while len(time_per_vault) > 0:
    next_step[next_step.index(min(next_step))] += time_per_vault.pop(0)

print(max(next_step))

