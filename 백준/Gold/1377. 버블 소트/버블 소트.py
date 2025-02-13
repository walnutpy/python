import sys
input = sys.stdin.readline

n = int(input())
arr = [[i,int(input())] for i in range(n)]

changed = sorted(arr,key=lambda x:x[1])

a = 0
for i in range(n):
    dist = changed[i][0] - i
    a = max(dist,a)

print(a+1)