input()
print(min(input().split(),key=lambda x:abs(int(x)-.1),default=0))