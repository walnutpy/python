import sys
input = sys.stdin.readline
all = [1,1,2,2,2,8]
get = list(map(int,input().split()))
for i in range(6):
    get[i] = all[i] - get[i]

print(*get)