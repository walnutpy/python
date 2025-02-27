import sys
input = sys.stdin.readline

n=int(input())
triangle = [list(map(int,input().split())) for _ in range(n)]

dp = [ [0] * len(row) for row in triangle ]
dp[0]=triangle[0]

for i in range(1,n):
    for j in range(len(triangle[i])):
        '''
        try:
            dp[i][j] = max(dp[i-1][j],dp[i-1][j+1]) + triangle[i][j]
        except:
            pass
        '''
        if j == 0:  # 해당 행의 첫 번째 요소는 바로 위 행의 첫 번째 요소만 더함
            dp[i][j] = dp[i-1][j] + triangle[i][j]
        elif j == len(triangle[i]) - 1:  # 마지막 요소는 바로 위 행의 마지막 요소만 더함
            dp[i][j] = dp[i-1][j-1] + triangle[i][j]
        else:  # 중간 요소는 위 행의 인접한 두 값을 비교
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
print(max(dp[n-1]))