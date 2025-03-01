import sys
input = sys.stdin.readline

n, k = map(int,input().split())
bag = [tuple(map(int,input().split())) for _ in range(n)] #w는 무게 / v는 가치

#dp 배열의 인덱스가 무게 그 안에 가치 그 가치의 최댓값 / dp가 가치, 그 안에 무게게
dp = [[0]*(k+1) for _ in range(n+1)]

for i in range(1,n+1):
    W,v = bag[i-1]
    for w in range(k+1):
        if w < W:
            dp[i][w] = dp[i-1][w]
        else:
            dp[i][w] = max(dp[i-1][w],dp[i-1][w-W]+v)

print(dp[n][k])