import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    a = list(map(int,input().split()))
    arr.append(a) 

elect = sorted(arr, key= lambda x: x[0])

dp = [1] * n #겹치는 수 구하기
for i in range(1,n):
    for j in range(i):
        if elect[j][1] < elect[i][1]:
            dp[i] = max(dp[i],dp[j]+1)

print(n-max(dp))