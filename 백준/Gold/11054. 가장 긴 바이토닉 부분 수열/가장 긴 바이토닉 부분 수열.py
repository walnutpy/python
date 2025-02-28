import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int,input().split()))



lis = [1] * n
for i in range(n):
    for j in range(i):
        if num[j] < num[i]:
            lis[i] = max(lis[i],lis[j]+1)

lds = [1]*n
for i in range(n-1,-1,-1):
    for j in range(i+1, n):
        if num[j] < num[i]:
            lds[i] = max(lds[i], lds[j]+1)

answer = 0
for i in range(n):
    answer = max(answer,lis[i]+lds[i]-1)
print(answer)